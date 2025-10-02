from bible_csv import bible_dict
import re

key_list = list(bible_dict.keys())

def bible_range():
    try:
        while True:
            start = input("🚩 시작 구절을 입력하세요 (예: 20:10) ▶ ")
            match = re.fullmatch(r"\d+:\d+", start)
            # 장:절 형식에 맞는 경우
            if match:
                # 해당 구절이 bible안에 있는 경우
                if start in bible_dict:
                    while True:
                        # 해당 구절부터 n개 출력
                        n = input("🔢 몇 개를 출력할까요? ▶ ")
                        # n이 숫자가 아닌 경우
                        if not n.isnumeric():
                            print("🚫 숫자만 입력해주세요!")
                        # n이 0 이하인 경우
                        elif int(n) <= 0:
                            print("🚫 0개는 출력할 수 없습니다.")
                        # n이 1 이상인 숫자를 입력받은 경우
                        else:
                            start_index = key_list.index(start)
                            for i in range(start_index, start_index + int(n)):
                                key = key_list[i]
                                print(f"{key}\n{bible_dict[key]}")
                            break
                    break
                # 해당 구절이 bible안에 없는 경우
                else:
                    print(f"🚫 [{start}]은 구절 내에 없습니다.")
            # 장:절 형식에 맞지 않는 경우
            else:
                print("🚫 올바르지 않은 입력입니다.")
                continue
    except IndexError:
        print("💁 마지막 구절 입니다.")