from bible_search import bible_search
from bible_range import bible_range
from bible_today import bible_today
from bible_word import bible_word

print(r"""
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
✨ 성경 검색 프로그램 ✨
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟""")

print(r"""
📌 메뉴
1️⃣ 구절 검색 🔍
2️⃣ 구절 범위 출력 📖➡️📖
3️⃣ 오늘의 성경 🍀
4️⃣ 성경 구문 검색 🔍
5️⃣ 종료 ❌👋
""")

while True:
    func = input("👉 메뉴를 선택하세요 ▶ ")
    match func:
        # 1. 구절 검색
        case "1":
            num = input("✏️ 검색할 구절을 입력하세요 (예: 20:10) ▶ ")
            bible_search(num)
        # 2. 구절과 숫자를 입력 후, 해당 구절부터 n개 출력
        case "2":
            bible_range()
        # 3. random 함수와 datetime 함수를 사용하여 오늘의 구절 1개를 출력
        case "3":
            bible_today()
        # 4. 단어와 숫자를 입력 후, 해당 단어가 포함된 구절 n개 출력
        case "4":
            word = input("✏️ 검색할 단어를 입력하세요.\n   대소문자는 신경쓰지 않으셔도 됩니다. 😉 ▶ ")
            bible_word(word)
        # 5. 프로그램 종료
        case "5":
            print("🙏 프로그램을 종료합니다. 🙏")
            break
        # _. 기능에 존재하지 않는 문자 또는 숫자가 입력된 경우
        case _:
            print("🚫 존재하지 않는 기능입니다!")