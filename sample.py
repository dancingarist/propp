
from openai import OpenAI
client = "sk-ngiwbvwbwbw"
client = openai.OpenAI()

import openai
import os
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む（セキュリティのため）
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # .envファイルにAPIキーを記載

# ユーザーの質問
user_input = "日本で有名なAI企業を3つ教えてください。その特徴も簡単に説明してください。"

# ChatGPT APIにリクエストを送信
response = client.chat.completions.create(
    model="gpt-4",  # GPT-4またはgpt-3.5-turboが使えます
    messages=[
        {"role": "system", "content": "あなたは親切で詳しいAIアシスタントです。"},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7,       # 出力のランダム性（0〜2）
    max_tokens=800,        # 出力の最大トークン数
    top_p=1.0,             # nucleus sampling
    frequency_penalty=0.0, # 同じ語の繰り返しを抑える
    presence_penalty=0.0   # 新しい話題を導入する傾向
)

# 結果を表示