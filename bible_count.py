import csv
from collections import Counter

def get_custom_stopwords():
    all_text = ""
    with open('bible_csv.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
                verse_text = row['Verse Text'].strip()
                all_text += " " + verse_text
    # 텍스트 추출
    words = all_text.split()  # 공백 기준으로 단어 분리
    word_freq = Counter(words)  # 단어 빈도 계산

    top_words = [word for word, _ in word_freq.most_common(30)] # 집합으로 묶기 (30개)

    custom_stopwords = set(top_words)   # 많이 나온 부분 확인 후, 세트로 묶기

    # 30개 이후 나오는 단어 set에 포함시키기
    custom_stopwords.update(['said','unto','son','name','come','upon','thee','son','Son','SON','upon','behold','man'])
    # print(custom_stopwords)
    # print(type(custom_stopwords))

    return set(top_words)
# said, unto, son, name, come, upon
# for word, freq in word_freq.most_common(30):  # 상위 30개 단어 출력
#     print(f"{word}: {freq}")

# {'will', 'be', 'of', 'shall', 'my', 'said', 'it', 'thy', 'is', 'a', 'in', 'unto', 'and', 'for', 'they', 'that', 'And', 'was', 'not', 'all', 'God', 'thou', 'to', 'with', 'his', 'I', 'he', 'the', 'said,', 'which'}