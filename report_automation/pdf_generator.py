from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io

def format_slovenian_date(date_str):
	months = [
		"januar", "februar", "marec", "april", "maj", "junij",
		"julij", "avgust", "september", "oktober", "november", "december"
	]
	dt = datetime.strptime(date_str, "%Y-%m-%d")
	return f"{dt.day}. {months[dt.month - 1]} {dt.year}"

def generate_pdf(data):
	datum = format_slovenian_date(data["datum"])
	ucitelj = data["ucitelj"]
	ucenci = data["ucenci"]
	vrsta_nasilja = data["vrsta"]
	opis = data["opis"]

	buffer = io.BytesIO()
	pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Regular.ttf'))
	c = canvas.Canvas(buffer, pagesize=A4)
	width, height = A4

	y = height - 3 * cm
	line_height = 14
	section_spacing = 20

	def draw_line(text, x=2 * cm, size=12, bold=False):
		nonlocal y
		c.setFont("Roboto", size)
		c.drawString(x, y, text)
		y -= line_height

	def draw_divider():
		nonlocal y
		c.setLineWidth(1)
		c.line(2 * cm, y, width - 2 * cm, y)
		y -= section_spacing

	# Title
	draw_line("POROČILO O INCIDENTU", size=16, bold=True)
	y -= section_spacing

	# Date
	draw_line(f"Datum: {datum}")
	y -= section_spacing

	# Teacher name
	draw_line(f"Ime in priimek učitelja: {ucitelj}")
	y -= section_spacing

	# Divider
	draw_divider()

	# Students
	draw_line("Udeleženi učenci:", size=13, bold=True)
	for ucenec in ucenci:
		draw_line(f"- {ucenec}", x=2.8 * cm)
	y -= section_spacing

	# Divider
	draw_divider()
	
	# Type
	draw_line(f"Vrsta nasilja: {vrsta_nasilja}")
	y -= section_spacing

	# Divider
	draw_divider()

	# Incident description
	draw_line("Opis incidenta:", size=13, bold=True)
	words = opis.split()
	line = ""
	max_chars = 95

	for word in words:
		if len(line + word) > max_chars:
			draw_line(line.strip(), x=2.8 * cm)
			line = ""
		line += word + " "
	if line:
		draw_line(line.strip(), x=2.8 * cm)
	y -= section_spacing

	# Final divider
	draw_divider()

	c.showPage()
	c.save()

	buffer.seek(0)
	return buffer.read()
