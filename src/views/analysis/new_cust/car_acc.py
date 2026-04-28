import pandas as pd
import streamlit as st
from datetime import datetime
from src.modules import streamlit_module as sm

df = pd.read_csv('src/resources/csv/교통사고.csv')
# src/resources/교통사고.csv라는 파일을 판다스로 읽어서 df라는 변수에 저장한다.

df['month'] = pd.to_datetime(df['month'])
# 전체 코드
# month 컬럼에 들어있는 값을 날짜 타입(datetime)으로 변환한 뒤, 다시 month 컬럼에 덮어씁니다.
# 이걸 왜 하냐면, 이렇게 datetime으로 바꿔야, 시계열 작업을 할수 있다.

st.header('자동차 사고 현황')
sm.make_space(2)
# st. header라는것은 큰 제목같은 글을 표현해주기 위해 씀
# sm은 아까 만든 별개의 변수명.  make space는 여백을 만들어라.  (2)는 두줄 여백을 만들어 띄워라. 라는 의미.



# ===============================
# 1. 데이터셋 (그리드)
# ===============================
total_data = []
# “total_data라는 이름의 변수에 빈 리스트를 할당한다”라는 의미. 즉, "데이터를 담기 위한 빈 리스트를 하나 만든다”

for gu in df['district'].unique():
    gu_data = df[df['district'] == gu].sort_values('month')
# df의 district라는 열 안에 있는, 중복되지 않은 값을 하나씩 꺼내서 gu라는 변수안에 넣어서 반복실행한다.

    if gu_data.empty:
        continue
# “gu_data가 비어 있으면, 이번 반복은 처리하지 말고 다음 반복으로 넘어가라”


    start_val = gu_data.iloc[0]['number']
    end_val = gu_data.iloc[-1]['number']
    diff = end_val - start_val

# gu_data의 첫 번째 행에서 'number' 컬럼 값을 가져와서 start_val에 저장한다.
# gu_data의 마지막 행에서 'number' 칼럼값을 가져와서 end_val에 저장한다.
# diff는 “차이값(diff)”을 계산하는 식으로, 시작값(start_val)과 끝값(end_val) 사이의 변화를 나타냄.
#  end val에서 start val값을 뺀 변화값을 가져와라 라는 의미.


    total_data.append((gu, int(end_val), int(diff)))
#  total_data에 하나의 튜플(gu, int(end_val), int(diff))를 추가하는것.
    

total_data.sort(key=lambda x: x[1], reverse=True)
#  total_data를 각 요소의 두 번째 값 기준으로 내림차순 정렬한다는 뜻입니다.
#  sort: 정렬하겠다, lambda x: 이름 없는(익명) 함수를 만드는 문법(x),  x[1]는 x의 두번째 요소를 뜻함. 
#  reverse=true : reverse=true는 '순서를 거꾸로 하겠다'라는 의미를 뜻함.
# key = 의 의미 : 정렬기준을 정하는 부분이라는 뜻.

#전체의미 : total_data의 데이터를 x의 2번째 요소를 기준으로 삼아, 내림차순으로 정렬하겠다.

total_df = pd.DataFrame(
    total_data,
    columns=['자치구', '전체 기간 기준 사고 횟수', '증감']
)

# total_df = pd.DataFrame( Pandas에서 데이터프레임(DataFrame)을 생성해서 변수 total_df에 저장한다는 의미.
# colums = ['자치구', '전체 기간 기준 사고 횟수', '증감'] 은 data frame 안에 각각의 열(칼럼) 이름을 지정하겠다는 의미.

st.dataframe(total_df, use_container_width=True, hide_index=True)
sm.make_space(5)

# total_df를 Streamlit 화면에 보기 좋게, 전체 폭으로, 인덱스 없이 깔끔하게 출력한다
 #total_df라는 pandas DataFrame을 표 형태로 보여줌.        st.dataframe(total_df, 
 # 테이블이 화면(컨테이너)의 전체 너비를 꽉 채우도록 만듭니다.  use_container_width=True
 # DataFrame의 index(왼쪽 숫자 열)를 숨깁니다.              hide_index=True

# ===============================
# 2. 기간 선택
# ===============================
month_list = df['month'].drop_duplicates().sort_values()
# “df의 month 열에서 중복된 월을 제거한 뒤, 남은 월들을 오름차순으로 정렬해서 month_list에 저장한다”


start_month, end_month = st.select_slider(
# # start_month, end_month = st.select_slider( 이 코드의 의미는 Streamlit에서 슬라이더로 선택한 “범위 값”을 두 변수에 나눠서 저장한다는 뜻입니다.

    '기간을 선택해주세요.',
    options=month_list.dt.strftime("%Y-%m").tolist(),
# pandas에서 날짜 데이터를 “연-월 문자열 리스트”로 바꾸는 코드입니다.


    value=(
        month_list.min().strftime("%Y-%m"),
        month_list.max().strftime("%Y-%m")

        # 이 코드는 날짜(월) 리스트에서 가장 이른 달과 가장 늦은 달을 뽑아서 "YYYY-MM" 형식의 문자열로 만드는 것입니다.
    )
)





start_date = datetime.strptime(start_month, "%Y-%m")
#문자열로 되어 있는 날짜를 Python의 datetime 객체로 변환하는 코드입니다.


end_date = datetime.strptime(end_month, "%Y-%m") 
options=month_list.dt.strftime("%Y-%m").tolist()
# 날짜 처리 + pandas 시리즈를 문자열 리스트로 변환하는 코드





# ===============================
# 3. 기간 필터링
# ===============================
filtered_df = df[
# DataFrame(df)을 조건에 따라 필터링하려는 코드의 시작 부분

    (df['month'] >= start_date) &
    (df['month'] <= end_date)
]

# df의 month 값이 start_date부터 end_date 사이에 있는 행만 선택하라


filtered_data = []
# filtered_data라는 이름의 리스트(list)를 생성


for gu in filtered_df['district'].unique():
    gu_data = filtered_df[filtered_df['district'] == gu].sort_values('month')

   # pandas(DataFrame)에서 구(district)별로 데이터를 나눠서 월(month) 순서대로 정렬하는 작업을 의미

    if gu_data.empty:
        continue

    # “gu_data가 비어 있으면, 아래 코드를 실행하지 말고 다음 반복으로 넘어가라”

    start_val = gu_data.iloc[0]['number']
    end_val = gu_data.iloc[-1]['number']
    diff = end_val - start_val

    # Pandas DataFrame인 gu_data에서 특정 열(number)의 처음 값과 마지막 값의 차이를 계산하는 의미

    filtered_data.append((gu, int(end_val), int(diff)))

# filtered_data 리스트에 (구 이름, 종료값(정수), 차이값(정수)) 형태의 데이터를 하나 추가한다


# ===============================
# 4. 카드 (Top5 / Bottom5)
# ===============================
filtered_data.sort(key=lambda x: x[2], reverse=True)

# filtered_data.sort(key=lambda x: x[2], reverse=True)는 파이썬에서 리스트를 특정 기준으로 정렬하는 코드
# lambda x: x[2]는 “각 요소 x에서 3번째 값(x[2])을 기준으로 하겠다”는 뜻
# reverse=True를 쓰면 내림차순(큰 값 → 작은 값)

top5 = filtered_data[:5]
bottom5 = filtered_data[-5:]

# 앞에서 5개 요소를 가져오겠다는 의미
# bottom5 = filtered_data[-5:]는 Python에서 리스트(또는 배열)의 마지막 5개 요소를 가져오는 코드

selected = top5 + bottom5
# 상위 5개와 하위 5개를 합쳐서 selected에 저장한다


cols = st.columns(5)
# 화면을 5개의 세로 컬럼(열)로 나누겠다는 의미


for i, (gu, val, diff) in enumerate(selected):
    cols[i % 5].metric(
        label=gu,
        value=val,
        delta=diff
    )

    # Streamlit에서 여러 개의 지표(metric)를 5개 컬럼에 나눠서 표시하는 로직