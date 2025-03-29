import os
import openai

import numpy as np

# client = OpenAI()
# OpenAI.api_key = "mykeyhere"

openai.api_key = os.getenv("OPENAI_API_KEY")

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
        
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        chat_response = response['choices'][0]['message']['content']
        print(f"ChatGPT: {chat_response}")
        messages.append({"role": "assistant", "content": chat_response})


if __name__ == "__main__":
    # input = input("Ask ChatGPT: ")
    # response = client.generate_response(input)
    # print(response)
    ChatBot()