import os
#import openai
from openai import OpenAI

import numpy as np

# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 


# client = OpenAI()
# OpenAI.api_key = "mykeyhere"

##### USTVARI VENV Z source venv/bin/activate #####
##### ZAGANJAJ IN NALAGAJ Z PYTHON3 IN PIP3 #####

#openai.api_key = os.getenv("OPENAI_API_KEY")

### INIT OPENAI CLIENT ###
# print("Key: ", os.getenv("OPENAI_API_KEY"))
# print("KLJUUUUC", os.environ['OPENAI_API_KEY'])

client = OpenAI(
    # api_key = os.environ.get("OPENAI_API_KEY"),
    api_key= os.getenv("OPENAI_API_KEY"),
    
)
# print("API key set successfully:", api_key),
# class Wrapper:
#     def __init__(self, api_key):
#         self.api_key = api_key
        
#     def generate_response(self, input):
#         response = client.chat.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": input},
#             ],
#         )
#         return response

def ChatBot():
    # response = client.chat.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": input},
    #     ],
    # )
    # return response
    messages = []
    while True:
        
        message = input("User: ")
        if message.lower() == "goodbye":
            break
        print("prsu sm sm")
        
        #messages.append({"role": "user", "content": message}) ne rabim tega ce mam key-pair v messages
        #mogoce bo treba to spremenit za continuous conversation?
        try:    
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "Help teachers resolve conflicts between students in primary school"},
                    {
                        "role": "user", 
                        "content": message,
                    }
                ],
            )
            response = completion.choices[0].message.content
            print(f"ChatGPT: {response}")
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=messages
            # )
            # chat_response = response['choices'][0]['message']['content']
            # print(f"ChatGPT: {chat_response}")
            # messages.append({"role": "assistant", "content": chat_response})
        except:
            print("Error: Unable to get a response from OpenAI API.")
            break
        


if __name__ == "__main__":
    # input = input("Ask ChatGPT: ")
    # response = client.generate_response(input)
    # print(response)
    ChatBot()