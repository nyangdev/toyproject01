bible = list()

with open("bible_csv.csv", "r", encoding="utf-8") as file:
    for i in file.readlines():
        # print(i)
        i = i.replace("\n", "").replace("\"", "")
        bible.append(i)

bible.remove(bible[0])
# print(bible)

bible_dict = dict()
for i in bible:
    # "," 기준으로 1번만 split -> 값이 2개로 나뉨
    i = i.split(",", 1)
    # i[0] : key, i[1] : value
    bible_dict[i[0]] = i[1]
# print(bible_dict)