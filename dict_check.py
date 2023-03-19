import openai
import key

openai.api_key = key.KEY

model ="gpt-3.5-turbo"
def dict(user_content):
    # query = '''
    # 규칙은 다음과 같다.
    # 1. 한글 사전에 단어가 있을 확률이 높다면 1이라고 말한다.
    # 2. 한글 사전에 단어가 없을 확률이 더 높다면 0이라고 말한다.
    # 3. 무조건 숫자로만 답한다.
    # 4. 마침표 사용금지
    # '''
    query = '''
    위 단어에 대해 한글 사전에 등재되어 있는지 판단해주세요.
    
    규칙은 다음과 같다.

    1. 한글 사전에 단어가 있을 확률이 높다면 1이라고 말한다.
    2. 한글 사전에 단어가 없을 확률이 더 높다면 0이라고 말한다.
    '''

    rule = '''
    person
    '''

    
    # print(user_content)
    query = user_content + query
    messages = [
        {"role" : "system", "content" : rule},
        {"role" : "user", "content" : query}
    ]


    completion = openai.ChatCompletion.create(model=model, messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    global response
    response = assistant_content
    print("사전 검증: ", response)
    if '1' in assistant_content:
        return True
    else:
        return False

# response = ""
# dict(input("input: "))
# print(response)