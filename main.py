from bible_search import bible_search
from bible_range import bible_range
from bible_today import bible_today
from bible_word import bible_word

print(r"""
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
✨ 성경 검색 프로그램 ✨
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟""")

print(r"""
📜 메뉴: 
      1️⃣ 오늘의 말씀 🕊️  
      2️⃣ 구절 찾기 🔍 
      3️⃣ 범위로 찾기 🔢
      4️⃣ 단어로 찾기 🔤
      5️⃣ 단어 모아보기 ☁️
      6️⃣ 말씀 담아두기 💌 
      7️⃣ 말씀 다시 읽기 🔄 
      8️⃣ 나가기 ❌

    👉 메뉴를 선택하세요 ▶
""")

while True:
    func = input("👉 메뉴를 선택하세요 ▶ ")
    match func:
        case "1":  # 1. random 함수와 datetime 함수를 사용하여 오늘의 구절 1개를 출력
            bible_today()

        case "2":  # 2. 구절 찾기
            num = input("✏️ 검색할 구절을 입력하세요 (예: 20:10) ▶ ")
            bible_search(num)

        case "3":  # 3. 구절과 숫자를 입력 후, 해당 구절부터 n개 출력
            bible_range()

        case "4":  # 4. 단어와 숫자를 입력 후, 해당 단어가 포함된 구절 n개 출력
            word = input("✏️ 검색할 단어를 입력하세요.\n   대소문자는 신경쓰지 않으셔도 됩니다. 😉 ▶ ")
            bible_word(word)

        case "5":  # 5. 단어로 모아보기
            pass

        case "6":  # 6. 말씀 담아두기
            pass

        case "7":  # 7. 말씀 다시 읽기
            pass

        case "8":  # 8. 종료
            print("🙏 프로그램을 종료합니다. 🙏")
            break
        # _. 기능에 존재하지 않는 문자 또는 숫자가 입력된 경우
        case _:
            print("🚫 존재하지 않는 기능입니다!")