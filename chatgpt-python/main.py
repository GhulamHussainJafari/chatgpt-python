from my_key import My_API_Key
import openai
openai.api_key = My_API_Key

messages = []

while True:
    message = input("user : ")
    if message:
        messages.append({"role": "user", "content": message})
        result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
        
    reply = result.choices[0].message.content
    print("Hussain's Chatbot : " + reply)
        