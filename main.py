import os
import openai
openai.api_key = "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"
messages=[]
while True:
    user_content = input("user : ")

    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role" : "user", "content" : f"{user_content}"})
    print(f"GPT : {assistant_content}")
