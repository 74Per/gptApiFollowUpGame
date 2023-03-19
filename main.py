import openai
import key
import dict_check

openai.api_key = key.KEY

model = dict_check.model

query = '''
로 시작하는 단어 하나 말해줘(동사금지, 단어만 말하기, 단어 뒤에 마침표 쓰지 않기).

'''

rule = '''
person
'''

while True:
    user_content = input("user : ")
    res = dict_check.dict(user_content)
    print(res)
    if  res == False:
        print("없는단어입니다. 컴퓨터의 승리입니다.")
        break
    user_content = user_content[-1]
    user_lastword = user_content
    # print(user_content)
    user_content+=query
    messages = [
        {"role" : "system", "content" : rule},
        {"role" : "user", "content" : f"{user_content}"}
    ]


    completion = openai.ChatCompletion.create(model=model, messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role" : "user", "content" : f"{user_content}"})
    print(f"GPT : {assistant_content}")

    if user_lastword !=assistant_content[0]:
        print("당신이 이겼습니다 축하합니다.")
        break