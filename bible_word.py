from bible_csv import bible_dict

def bible_word(word):
    cnt = 0
    word_dict = dict()
    for i in bible_dict:
        if word.lower() in bible_dict[i].lower():
            cnt += 1
            word_dict[i] = bible_dict[i]
    if cnt == 0:
        print("🚫 구절 안에 존재하지 않는 단어 입니다.")
    else:
        print(f"🔍 [{word}] 포함된 구절 {cnt}개를 찾았습니다!")
        # [{word}] 포함된 구절 n개 출력
        while True:
            n = input("🔢 몇 개를 출력할까요? ▶ ")
            # n이 숫자가 아닌 경우
            if not n.isnumeric():
                print("🚫 숫자만 입력해주세요!")
            # n이 0 이하인 경우
            elif int(n) <= 0:
                print("🚫 0개는 출력할 수 없습니다!")
            # n이 1 이상인 숫자를 입력받은 경우
            else:
                # n이 cnt(word_dict에 저장된 데이터 수)보다 큰 경우
                if int(n) > cnt:
                    print(f"🚫 {cnt}개 이하로 입력해주세요!")
                    continue
                # 1 <= n <= cnt 인 경우
                else:
                    new_cnt = 0
                    # word_dict 내에서 한 구절씩 출력
                    for i in word_dict:
                        # new_cnt가 n(출력할 갯수) 보다 작은 동안 동작
                        if new_cnt < int(n):
                            # new_cnt : 출력한 갯수
                            new_cnt += 1
                            print(f"[{i}]\n{word_dict[i]}")
                break