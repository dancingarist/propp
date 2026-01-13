import streamlit as st
import csv

st.title("ボタンだけのアプリ")

# ① 最初のボタン
if st.button("押してね"):
    st.write("ボタンが押されました！")

# ② CSV読み込み
CSV_FILE = "story.csv"
all_rows = []

try:
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_rows.append(row)
except FileNotFoundError:
    st.error("CSVファイルが見つかりません。")
    st.stop()

# ③ CSV表示用ボタン
if st.button("おせ"):
    st.write("CSVファイルの中身はこちらです")
    st.dataframe(all_rows)   # ← 表形式で表示











