from bible_csv import bible_dict
import os

folder = "bible_save"
key_list = list(bible_dict.keys())

def bible_file():
    # 저장용 폴더 만들기
    os.makedirs(folder, exist_ok=True)

    file_name = input("파일명을 입력해주세요 : ")

    file_path = os.path.join(folder, file_name)

    # 파일이 이미 존재하면 append, 없으면 새로 만들기

    while 1:
        user_write = input("저정하고 싶은 구절을 입력하세요 (ex. 1:1) : ")

        if user_write not in key_list:
            print("존재하지 않는 구절입니다. 다시 입력해주세요.")
            continue

        with open(file_path, "a", encoding="utf-8") as file:

            file.write(f"{bible_dict[user_write]}\n")

        while 1:

            y_or_n = input("추가 저장을 원하시나요? (원하면 y, 원하지않으시면 n을 입력해주세요.) : ")

            if y_or_n == "y":
                break
            elif y_or_n == "n":
                break
            else:
                # 잘못된 입력 exception 보내줘야함
                print("y 또는 n만 입력해주세요.")
                continue

        if y_or_n == "n":
            break