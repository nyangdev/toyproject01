from bible_csv import bible_dict


def bible_word(word):
    cnt = 0
    word_dict = dict()
    target = word.lower()

    for i in bible_dict:
        # 구절을 소문자로 바꾸고 공백 기준으로 단어 분리
        words_in_verse = bible_dict[i].lower().split()
        # 정확히 일치하는 단어가 있는지 확인
        if target in words_in_verse:
            cnt += 1
            word_dict[i] = bible_dict[i]

    if cnt == 0:
        print("🚫 구절 안에 존재하지 않는 단어 입니다.")
    else:
        print(f"🔍 [{word}] 포함된 구절 {cnt}개를 찾았습니다!")
        while True:
            n = input("🔢 몇 개를 출력할까요? ▶ ")
            if not n.isnumeric():
                print("🚫 숫자만 입력해주세요!")
            elif int(n) <= 0:
                print("🚫 0개는 출력할 수 없습니다!")
            elif int(n) > cnt:
                print(f"🚫 {cnt}개 이하로 입력해주세요!")
            else:
                new_cnt = 0
                for i in word_dict:
                    if new_cnt < int(n):
                        new_cnt += 1
                        print(f"[{i}]\n{word_dict[i]}")
                break
