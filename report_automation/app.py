#from flask import Flask, request, send_file, render_template
from flask import Flask, request, jsonify, send_file, render_template
from pdf_generator import generate_pdf
import os
from io import BytesIO

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("report.html")

@app.route("/generate-pdf", methods=["POST"])
def create_pdf():
    data = request.get_json()
    pdf_bytes = generate_pdf(data)
    return send_file(
        BytesIO(pdf_bytes),
        mimetype='application/pdf',
        as_attachment=True,
        download_name='porocilo.pdf'
    )

@app.route("/api/transcribe", methods=["POST"])
def create_audio():
    
	print("Tukajs em")
	if 'audio' not in request.files:
		return jsonify({'error': 'No audio file provided'}), 400

	audio_file = request.files['audio']
		# You can now process the audio_file as needed
		# For example, save it to disk or pass it to a transcription service

		# Example: Save the file to disk
	audio_file.save('uploaded_recording.wav')

		# Placeholder for transcription result
	transcription_result = 'Transcribed text goes here'

	return jsonify({'transcription': transcription_result})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
