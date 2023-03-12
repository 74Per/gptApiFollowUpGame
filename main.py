# module import
# python3 -m pip install openai

import openai
import json

# OpenAI API 키 설정
openai.api_key = "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"

# API 요청 보내기
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci", # GPT 모델의 엔진 이름
        prompt=prompt, # 대화 시작 문장
        max_tokens=60, # 생성할 텍스트의 최대 길이
        n=1, # 생성할 텍스트의 개수
        stop=None, # 생성할 텍스트의 종료 조건
        temperature=0.7, # 다양한 출력을 생성하기 위한 온도 매개변수
    )
    message = response.choices[0].text.strip()
    return message

# 대화 생성 예제
while True:
    prompt = input("You: ")
    prompt = prompt[-1]
    prompt = "'" + prompt + "'"
    prompt += "로 시작하는 2글자 단어 하나 알려줘"
    response = generate_text(prompt)
    print("AI: " + response)