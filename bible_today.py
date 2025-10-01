from bible_csv import bible_dict
import random
from datetime import datetime

key_list = list(bible_dict.keys())

def bible_today():
    # now_hour : 현재 시간
    now_hour = datetime.now().hour
    hour = ""
    if now_hour < 12:
        hour = f"오전 {now_hour}시"
    elif now_hour == 12:
        hour = "정오"
    else:
        now_hour = now_hour - 12
        if now_hour < 12:
            hour = f"오후 {now_hour}시"
        elif now_hour == 12:
            hour = "자정"

    # random.seed() : 현재 시간으로 seed를 고정
    random.seed(now_hour)
    # randint(a, b) : a <= N <= b
    random_num = random.randint(0, len(bible_dict) - 1)
    # 24시 형식으로 표현되는 현재 시간을 12시 형식으로 변경
    key = key_list[random_num]
    print(f"🍀 {hour}의 구절")
    print(f"[{key}]\n{bible_dict[key]}")