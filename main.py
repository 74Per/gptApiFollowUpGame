import openai
openai.api_key = "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"
messages=[]
while True:
    user_content = input("user : ")
    user_content = user_content[-1]
    print(user_content)
    user_content+="로 시작하는 단어 하나 말해줘"
    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role" : "user", "content" : f"{user_content}"})
    print(f"GPT : {assistant_content}")
