from bible_csv import bible_dict
import os

folder = "bible_save"

def bible_file_open():
    """
    1. 저장되어있는 파일명 목록을 조회할 수 있도록 해준다
    2. 조회를 하고자하는 파일명을 입력받는다
    3. 조회된 파일을 read해서 프린트한다
    """

    # 예외처리
    """
    - 저장하고 싶은 구절을 입력하세요 부분에서 KeyError 발생시에 종료돼서 기능 선택으로 바로 넘어가는게 아니라
    다시 구절 부분 입력하게 하는게 좋을듯
    """

    print("저장되어있는 파일 목록을 출력합니다.")

    # 폴더 생성이 안되어있으면 -> 파일 자체를 생성한적이 없는거임 -> 파일 목록이 없다고 하고 continue
    if os.path.isdir(f'{folder}'):
        files = os.listdir(folder)

        # 생성된 폴더 안에 생성된 파일들 출력하기
        if files:
            for f in files:
                print(f)

            while 1:

                file_choice = input("출력하고자하는 파일명을 입력하세요 : ")

                file_path = os.path.join(folder, file_choice)

                if os.path.exists(file_path):

                    if os.path.getsize(file_path) == 0:
                        print("비어있는 파일입니다.")
                        break

                    else:
                        print(f"[{file_choice}] 파일 내용을 출력합니다.")
                        with open(file_path, "r", encoding="utf-8") as file:
                            lines = file.read().splitlines()
                            for i in lines:
                                print(f"{i}")
                        break

                else:
                    print("존재하지않는 파일명입니다.")
                    continue

        else:
            # 이중 검증
            print("폴더는 있지만 저장된 파일이 없습니다.")

    else:
        print("저장된 폴더와 파일이 없습니다. 파일 저장 후 조회 기능을 이용해주세요.")

    """
    유저가 파일명 선택
    선택한 파일 내용 출력해준다고 하고
    출력해줌
    """

    # while 1:
    #
    #     file_choice = input("출력하고자하는 파일명을 입력하세요 : ")
    #
    #     file_path = os.path.join(folder, file_choice)
    #
    #     if os.path.exists(file_path):
    #
    #         if os.path.getsize(file_path) == 0:
    #             print("비어있는 파일입니다.")
    #             break
    #
    #         else:
    #             print(f"[{file_choice}] 파일 내용을 출력합니다.")
    #             with open(file_path, "r", encoding="utf-8") as file:
    #                 lines = file.read().splitlines()
    #                 for i in lines:
    #                     print(f"{i}")
    #             break
    #
    #     else:
    #         print("존재하지않는 파일명입니다.")
    #         continue

    # 예외 case
    """
    1. 존재하지않는 파일명 입력
    2. 파일은 존재하는데 빈 파일일때
    """

    """
    존재하지않는 파일명일때 바로 기능 선택으로 돌아가는게 아니라 다시 입력받기
    """