import os
from openai import OpenAI

OpenAI().api_key=os.environ["OPENAI_API_KEY"]

client = OpenAI()


response = client.responses.create(
    model="gpt-4.1",
    input="ドラゴンボールの漫画10巻までに出てくるキャラクターについてプロップ理論を用いてキャラクターを分類して" 
)
print(response.output_text)

