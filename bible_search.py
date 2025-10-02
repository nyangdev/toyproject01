from bible_csv import bible_dict
import re

def bible_search(num):
    match = re.fullmatch(r"\d+:\d+", num)
    # print(match)
    if match:
        if num in bible_dict:
            print(f"[{num}]\n{bible_dict[num]}")
        else:
            print(f"🚫 {num}은 구절 내에 없습니다.")
    else:
        print("🚫 올바르지 않은 입력입니다.")