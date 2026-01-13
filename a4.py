import csv
import streamlit as st

# ======================
# 作品選択
# ======================
st.title("プロップ31機能 検索システム")

work = st.selectbox(
    "作品を選択してください",
    ["（選択してください）", "羅生門", "藪の中"]
)

if work == "（選択してください）":
    st.stop()

# ======================
# 作品ごとの設定
# ======================
if work == "羅生門":
    CSV_FILE = "rasyou2.csv"
    TITLE = "【羅生門】プロップ31機能 検索"
    PERSON_LIST = ["下人", "老婆", "京都の人々", "死骸", "楼上の人物"]

    def person_match(target_person, person):
        if person == "京都の人々":
            return "京都" in target_person
        return person in target_person

elif work == "藪の中":
    CSV_FILE = "story.csv"
    TITLE = "【藪の中】プロップ31機能 検索"
    PERSON_LIST = [
        "木樵", "死んだ武士", "検非違使", "通行人", "捕吏",
        "多襄丸", "武弘", "真砂", "姥", "観世音菩薩"
    ]

    def person_match(target_person, person):
        if not target_person:
            return False
        return person in target_person

# ======================
# 本体UI
# ======================
st.title(TITLE)

# CSV読み込み
all_rows = []
try:
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_rows.append(row)
except FileNotFoundError:
    st.error("CSVファイルが見つかりません。")
    st.stop()

# 章選択
chapters = sorted({row["章"] for row in all_rows}, key=lambda x: int(x))

if "selected_chapter" not in st.session_state:
    st.session_state.selected_chapter = chapters[0]

st.subheader("章を選択")
cols = st.columns(len(chapters))
for col, chapter in zip(cols, chapters):
    with col:
        if st.button(chapter):
            st.session_state.selected_chapter = chapter

selected_chapter = st.session_state.selected_chapter
st.markdown(f"**選択中の章：第 {selected_chapter} 章**")

# 章で絞り込み
chapter_rows = [row for row in all_rows if row["章"] == selected_chapter]

# この章に登場する人物だけ抽出
available_persons = []
for person in PERSON_LIST:
    for row in chapter_rows:
        if person_match(row["対象人物"], person):
            available_persons.append(person)
            break

available_persons = list(dict.fromkeys(available_persons))

# 登場人物で絞り込み
st.subheader("登場人物で絞り込む（任意）")
selected_person = st.selectbox(
    "登場人物を選択してください",
    ["（指定なし）"] + available_persons
)

filtered_rows = chapter_rows
if selected_person != "（指定なし）":
    filtered_rows = [
        row for row in filtered_rows
        if person_match(row["対象人物"], selected_person)
    ]

# 一覧表示
st.subheader("該当機能一覧")

if not filtered_rows:
    st.warning("該当するデータがありません。")
    st.stop()

labels = [
    f"{i+1}: {row['機能']}（{row['対象人物']}）"
    for i, row in enumerate(filtered_rows)
]

selected_label = st.radio("表示したい機能を選択してください", labels)
selected = filtered_rows[labels.index(selected_label)]

# 詳細表示
st.markdown("---")
st.markdown(f"### 【該当プロップ機能】{selected['機能']}")
st.markdown(f"**【機能説明】**  \n{selected['機能説明']}")
st.markdown(f"**【場面説明】**  \n{selected['場面説明']}")
st.markdown(f"**【対象人物】**  \n{selected['対象人物']}")
st.markdown(f"**【本文要約】**  \n{selected['本文要約']}")
