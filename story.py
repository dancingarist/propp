import csv

CSV_FILE = "story.csv"

# 章番号を入力
chapter_input = input("章の番号を入力してください: ")

rows = []

# CSV読み込み
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["章"] == chapter_input:
            rows.append(row)

# 該当章が存在しない場合
if not rows:
    print("指定された章は見つかりませんでした。")
    exit()

# 機能一覧を表示
print("\n【機能一覧】")
for i, row in enumerate(rows, start=1):
    print(f"{i}: {row['機能']}")

# 機能を選択
choice = input("\n表示したい機能の番号を入力してください: ")

# 入力チェック
if not choice.isdigit() or not (1 <= int(choice) <= len(rows)):
    print("無効な番号です。")
    exit()

selected = rows[int(choice) - 1]

# 結果表示
print("\n-------------------------")
print(f"【該当プロップ機能】{selected['機能']}")
print(f"【機能説明】\n{selected['機能説明']}")
print(f"【場面説明】\n{selected['場面説明']}")
print(f"【対象人物】\n{selected['対象人物']}")
print(f"【本文要約】\n{selected['本文要約']}")
print("-------------------------")
