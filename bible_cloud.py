import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import re
from bible_count import get_custom_stopwords


def show_chapter_wordcloud(chapter_number):
    all_text = ""

    with open('bible_csv.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:  # CSV 파일의 각 줄을 반복하면서 처리, row는 딕셔너리 형태로 한 줄의 데이터를 담음
            reference = row['Verse Reference'].strip()  # # bible.csv안 'Verse Reference' 열에서 구절 내용 추출
            verse_text = row['Verse Text'].strip()  # # bible.csv안 'Verse Text' 열에서 구절 내용 추출

            # 장 번호 추출 (예: '1:1' → 1)
            match = re.match(r'^(\d+):\d+', reference)
            if match and int(match.group(1)) == chapter_number:
                all_text += " " + verse_text
    """csv.DictReader는 CSV 파일을 딕셔너리 형태로 읽는 도구
    각 행(row)을 {열이름: 값} 형태로 반환
    Verse Number,Verse Text
    1:1,태초에 하나님이 천지를 창조하시니라
    """
    """
    {'Verse Number': '1:1', 'Verse Text': '태초에 하나님이 천지를 창조하시니라'}
    """
    # CSV (csv.DictReader)	한 줄씩 읽으며 처리	with open 안에서 반복 필요
    # JSON (json.load)	전체를 한 번에 읽어 메모리에 저장	with open 밖에서도 반복 가능

    if not all_text:
        print(f"🚫 {chapter_number}장에서 구절을 찾을 수 없습니다!")
        return

    # 불용어 처리
    custom_stopwords = get_custom_stopwords()
    custom_stopwords.update(['said','unto','son','name','come','upon','thee','son','Son','SON','upon','behold','man','let','saw','good','every'])
    # 불용어 직접 추가 하기
    stopwords = STOPWORDS.union(custom_stopwords)

    # 마스크 이미지
    mask_img = np.array(Image.open('cross.png'))
    mask_img = 255 - mask_img

    # 워드클라우드 생성
    wordcloud = WordCloud(
        # font_path='Goyang.ttf',
        width=mask_img.shape[1],
        height=mask_img.shape[0],
        background_color='white',
        mask=mask_img,
        stopwords=stopwords
    ).generate(all_text)

    # 출력
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    # plt.title(f"{chapter_number}장 워드클라우드", fontsize=16)
    plt.show()

def bible_cloud():
    try:
        chapter_input = int(input("☁️ 어느 장의 워드클라우드를 보고 싶으신가요? (예: 1~50) ▶ "))
        show_chapter_wordcloud(chapter_input)
    except ValueError:
        print("🚫 숫자만 입력해주세요!")