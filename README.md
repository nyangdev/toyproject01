# ✝️️ 창세기 in Terminal: 말씀 한 줄, 은혜 한 모금 🕊️
---

> **🌟 "태초에 하나님이 천지를 창조하시니라." (창세기 1:1)**

- 2025.09.29 - 2025.10.02
- 영문 성경을 찾아 읽을 수 있는 프로그램입니다. 
- 원하는 구절을 찾아보고 오늘의 말씀도 확인해보세요.
---

## 🗂️ 프로젝트 구조

```markdown
.
├── README.md
├── __pycache__
├── bible.txt  # 원시 데이터
├── bible_cloud.py
├── bible_count.py
├── bible_csv.csv  # 원천 데이터
├── bible_csv.py  # 데이터 전처리
├── bible_file.py
├── bible_file_open.py
├── bible_range.py
├── bible_search.py
├── bible_today.py
├── bible_word.py
├── cross.png
├── main.py  # entry point
└── requirements.txt

2 directories, 15 files
```

---

## 🛠️ 프로그램 환경

* 📦 Conda *25.7.0*
* 🐍 Python *3.13.5*

## 🚀 시작하기

### Conda 환경 저장
```bash
conda export --file requirements.txt
```

### Conda 환경 생성

```bash
conda create --name amen --file ./requirements.txt
```

### Conda 환경 활성화

```bash
conda activate amen
```

### 파일 실행

```bash
python bible_search.py
```

## ✨ 메뉴 소개 🕊️

```bash
📜 메뉴: 
  1️⃣ 오늘의 말씀 🕊️  
  2️⃣ 구절 찾기 🔍 
  3️⃣ 범위로 찾기 🔢
  4️⃣ 단어로 찾기 🔤
  5️⃣ 단어 모아보기 ☁️
  6️⃣ 말씀 담아두기 💌 
  7️⃣ 말씀 다시 읽기 🔄 
  8️⃣ 나가기 ❌

👉 메뉴를 선택하세요 ▶ 
```
---
### 1️⃣ 오늘의 말씀 🕊️
   
   * 초기 화면에서 `1`을 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 1
     ```
     
   * [TBD - 로직 반영해서 내용 담기] 시간 마다 오늘의 말씀이 변경됩니다. 1시간 뒤에는 다른 내용이겠죠?

     ```bash
     🍀 오전 10시의 구절
     [39:21]
     But the LORD was with Joseph, and shewed him mercy, and gave him favour in the sight of the keeper of the prison.
     ```
---
### 2️⃣ 구절 찾기 🔍
   
   * 초기 화면에서 `2`를 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 2
     ```
   
   * 읽고싶은 장과 절을 `1:1` 형식으로 입력해주세요.

     ```bash
     ✏️ 검색할 구절을 입력하세요 (예: 20:10) ▶ 20:10
     ```
   
   * [TBD - 실제 결과 반영] 결과를 볼 수 있습니다.

     ```bash
     [20:10]
     And Abimelech said unto Abraham, What sawest thou, that thou hast done this thing?
     ```

   * [TBD - 실제 예외 처리 반영] 예외 처리 결과를 볼 수 있습니다.

     - `숫자:숫자` 형식으로 입력했지만 dictionary에 존재하지 않는 경우 입니다.
         ```bash
         ✏️ 검색할 구절을 입력하세요 (예: 20:10) ▶ 11:56
         🚫 11:56은 구절 내에 없습니다!
         ```

     - `숫자:숫자` 형식으로 입력하지 않은 경우 입니다.
         ```bash
         ✏️ 검색할 구절을 입력하세요 (예: 20:10) ▶ bible 1:1
         🚫 올바르지 않은 입력입니다!
         ```
---
### 3️⃣ 범위로 찾기 🔢
   
   * 초기 화면에서 `3`을 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 3
     ```
   
   * 구절의 시작점을 입력해주세요.

     ```bash
     🚩 시작 구절을 입력하세요 (예: 20:10) ▶ 20:10
     ```
        * `숫자:숫자` 형식이 아닌 경우, `문자 또는 숫자`만 입력된 경우 다시 입력할 수 있습니다.

   * 보고싶은 구절의 수를 입력해주세요.

     ```bash
     🔢 몇 개를 출력할까요? ▶ 3
     ```
        * 출력할 구절의 갯수가 유효하지 않은 경우 다시 입력할 수 있습니다. 
        * 최대 몇 개까지 볼 수 있는지 확인해보세요!
        
   * [TBD - 실제 결과 반영] 결과를 볼 수 있습니다.

     ```bash
     [20:10]
     And Abimelech said unto Abraham, What sawest thou, that thou hast done this thing?
     [20:11]
     And Abraham said, Because I thought, Surely the fear of God is not in this place; and they will slay me for my wife's sake.
     [20:12]
     And yet indeed she is my sister; she is the daughter of my father, but not the daughter of my mother; and she became my wife.
     ```
     
   * [TBD - 실제 예외 처리 반영] 예외 처리 결과를 볼 수 있습니다.

     - `숫자:숫자` 형식으로 입력했지만 dictionary에 존재하지 않는 경우 입니다.
         ```bash
         🚩 시작 구절을 입력하세요 (예: 20:10) ▶ 1:33
         🚫 [1:33]은 구절 내에 없습니다!
         ```
       
     - `숫자:숫자` 형식으로 입력하지 않은 경우 입니다.
         ```bash
         🚩 시작 구절을 입력하세요 (예: 20:10) ▶ abcd
         🚫 올바르지 않은 입력입니다!
         ```
     
     - 출력하고 싶은 데이터의 갯수를 입력합니다.
       - `숫자`를 입력하지 않은 경우입니다.
           ```bash
           🔢 몇 개를 출력할까요? ▶ a
           🚫 숫자만 입력해주세요!
           ```
         
       - `0`을 입력한 경우입니다.
           ```bash
           🔢 몇 개를 출력할까요? ▶ 0
           🚫 0개는 출력할 수 없습니다!
           ```
       
       - `존재하는 데이터 갯수보다 큰 수`를 입력한 경우입니다.
           ```bash
           🔢 몇 개를 출력할까요? ▶ 10000
           ...
           [50:26]
           So Joseph died, being an hundred and ten years old: and they embalmed him, and he was put in a coffin in Egypt.
           💁 마지막 구절 입니다.
           ```
---
### 4️⃣ 단어로 찾기 🔤

   * 초기 화면에서 `4`을 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 4
     ```
   
   * 검색할 단어를 입력해주세요.
    
     ```bash
     ✏️ 검색할 단어를 입력하세요.
        대소문자는 신경쓰지 않으셔도 됩니다. 😉 ▶ heaven
     ```
   
   * 보고싶은 구절의 수를 입력해주세요.

     ```bash
     🔍 [heaven] 포함된 구절 12개를 찾았습니다!
     🔢 몇 개를 출력할까요? ▶ 3
     ```
        * 검색한 단어가 포함된 구절 수를 확인해보세요!
        * 출력할 구절의 갯수가 유효하지 않은 경우 다시 입력할 수 있습니다.

   * [TBD - 실제 결과 반영] 결과를 볼 수 있습니다.

     ```bash
     [1:1]
     In the beginning God created the heaven and the earth.
     [1:9]
     And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so.
     [1:14]
     And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
     ```
   
   * [TBD - 실제 예외 처리 반영] 예외 처리 결과를 볼 수 있습니다.

     - 검색한 단어가 dictionary에 존재하지 않는 경우 입니다.
         ```bash
         ✏️ 검색할 단어를 입력하세요.
            대소문자는 신경쓰지 않으셔도 됩니다. 😉 ▶ hell
         🚫 구절 안에 존재하지 않는 단어 입니다.
         ```
       
     - 출력하고 싶은 데이터의 갯수를 입력합니다.
       - `숫자`를 입력하지 않은 경우입니다.
           ```bash
           🔢 몇 개를 출력할까요? ▶ one
           🚫 숫자만 입력해주세요!
           ```
         
       - `0`을 입력한 경우입니다.
           ```bash
           🔢 몇 개를 출력할까요? ▶ 0
           🚫 0개는 출력할 수 없습니다!
           ```
       
       - `존재하는 데이터 갯수보다 큰 수`를 입력한 경우입니다.
           ```bash
           ✏️ 검색할 단어를 입력하세요.
              대소문자는 신경쓰지 않으셔도 됩니다. 😉 ▶ heaven
           🔍 [heaven] 포함된 구절 12개를 찾았습니다!
           🔢 몇 개를 출력할까요? ▶ 13
           🚫 12개 이하로 입력해주세요!
           ```
---
### 5️⃣ 단어 모아보기 ☁️ 

   * 초기 화면에서 `5`를 입력하면 단어를 모은 그림을 볼 수 있습니다. 

      ```bash
      👉 메뉴를 선택하세요 ▶ 5
      ```

   * [TBD]장 번호이모그림으로 볼 수 있습니다.
    
      ```bash
      🔤 몇 장의 단어를 모아볼까요? (1 ~ 50) 👉 30
      ```
    
   * [TBD - 실제 결과 반영] 그림을 확인해보세요!

     ```bash
     그림
     ```
---
### 6️⃣ 말씀 담아두기 💌 

   * 초기 화면에서 `6`을 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 6
     ```
     
   * [TBD - 입력 프롬프트 확인하기] 이름을 입력합니다.
    
     ```bash
     🔤 이름을 알려주세요. 👉 30
     ```
    
   * [TBD - 입력 프롬프트 확인하기] 저장할 구문을 입력합니다. 

     ```bash
     🔤 구문을 알려주세요 👉 10:10
     ```
---
### 7️⃣ 말씀 다시 읽기 🔄 

   * 초기 화면에서 `7`을 입력하면 진입할 수 있습니다.

     ```bash
     👉 메뉴를 선택하세요 ▶ 7
     ```
 
   * [TBD - 입력 프롬프트 확인하기] 이름을 입력합니다.
    
     ```bash
     🔤 이름을 알려주세요. 👉 30
     ```
    
   * [TBD - 입력 프롬프트 확인하기] 저장했던 내용을 다시 읽어봅니다. 

     ```bash
     🔤 구문을 알려주세요 👉 10:10
     ```
---

## 개발 후기 
- 핵심 코드와 기능, 고민했던 내용을 간략하게 남겨둡니다.

#### 강지연
- 기억에 남는 코드
    ```bash
    import re
    match = re.fullmatch(r"\d+:\d+", num)
    ```
- 고민했던 내용
  1) 입력받은 num이 '숫자:숫자' 형식이고, bible_dict 안에 있다면
     > 정상 출력
  2) 입력받은 num이 '숫자:숫자' 형식이지만, bible_dict 안에 없다면
     > '해당 num은 구절 내에 없습니다' 출력
  3) 입력받은 num이 '숫자:숫자' 형식이 아니라면
     > '올바르지 않은 입력입니다' 출력
      
- 해결 방법
  > idea 1. ":" in num ?
     * 입력받은 문자열 안에 ":"이 있는지 확인
     * "숫자:숫자", "숫자:문자", "문자:숫자", "문자:문자" 등 입력받은 문자열 안에 ":"이 있기만 하면 True -> X
  > idea 2. 정규표현식 ?
     * 정규표현식을 사용하여 입력받은 문자열이 패턴과 일치하는지 확인
     * \d+:\d+ -> \d(숫자 0~9)가 +(1개 이상) 있고, 그 사이에 ":"이 있는 형태
     * re.match : 시작 문자열에서만 확인
     * '1:1 창세기'가 입력된 경우, 시작 문자열에 해당 패턴이 존재하므로 -> X
     * re.search : 전체 문자열에서 확인
     * '창세기 1:1'을 입력받은 경우, 문자열 내에 해당 패턴이 존재하므로 -> X
     * `re.fullmatch : 문자열 전체가 패턴과 일치`
     * `입력받은 문자열 전체가 패턴과 정확하게 일치하면 True -> O`

#### 허무지
- 기억에 남는 코드
    > bible_line += " " + line.strip()

- 고민했던 내용
    - 원시 데이터를 장, 절, 성경 구절로 변경하는 과정에서 성경 구절에 있는 `\n`이 예상과는 다르게 동작
    - 성경 구절 안에 있던 개행 문자가 한 절의 데이터를 나누면서 두 줄의 데이터가 생김
    - 하나의 절에 해당하는 구절 내에서는 줄바꿈을 없애고자 함
    - 해결 방법
    - `str` 내장 함수 중 strip를 적용하여 내용을 합침
- 후기
    - 데이터 전처리를 하면서 이스케이프 문자를 처리하는 여러 방법이 있다는 점을 알게 됨
    - strip을 사용하면 기존 개행 정보를 제거하여, 팀원이 구절 내용 전체를 큰따옴표로 감싼 방식을 보고 배움

---

> **✝️ "요셉이 죽으매 그들이 그의 몸에 향 재료를 넣고 애굽에서 입관하였더라." (창세기 50:26) 🌟**