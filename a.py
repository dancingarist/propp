import streamlit as st
import csv
st.title("ボタンだけのアプリ")

if st.button("押してね"):
    st.write("ボタンが押されました！")

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


if st.button(all_rows = [0]):
    st.write("ボタンが押されました！")







