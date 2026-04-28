import streamlit as st
import pandas as pd
from datetime import datetime
from src.modules import streamlit_module as sm

st.header('자동차 등록 현황')
sm.make_space(2)

# ===============================
# 데이터 로드
# ===============================
df = pd.read_csv('src/resources/csv/자동차등록수.csv')
df['month'] = pd.to_datetime(df['month'])



# ===============================
# 1. 데이터셋 (그리드)
# ===============================
total_data = []

for gu in df['district'].unique():
    gu_data = df[df['district'] == gu].sort_values('month')

    if gu_data.empty:
        continue

    start_val = gu_data.iloc[0]['number']
    end_val = gu_data.iloc[-1]['number']
    diff = end_val - start_val

    total_data.append((gu, int(end_val), int(diff)))

total_data.sort(key=lambda x: x[1], reverse=True)

total_df = pd.DataFrame(
    total_data,
    columns=['자치구', '전체 기간 기준 등록 대수', '증감']
)

st.dataframe(total_df, use_container_width=True, hide_index=True)
sm.make_space(5)



# ===============================
# 2. 기간 선택
# ===============================
month_list = df['month'].drop_duplicates().sort_values()

start_month, end_month = st.select_slider(
    '기간을 선택해주세요.',
    options=month_list.dt.strftime("%Y-%m").tolist(),
    value=(
        month_list.min().strftime("%Y-%m"),
        month_list.max().strftime("%Y-%m")
    )
)

start_date = datetime.strptime(start_month, "%Y-%m")
end_date = datetime.strptime(end_month, "%Y-%m")



# ===============================
# 3. 기간 필터링
# ===============================
filtered_df = df[
    (df['month'] >= start_date) &
    (df['month'] <= end_date)
]

filtered_data = []

for gu in filtered_df['district'].unique():
    gu_data = filtered_df[filtered_df['district'] == gu].sort_values('month')

    if gu_data.empty:
        continue

    start_val = gu_data.iloc[0]['number']
    end_val = gu_data.iloc[-1]['number']
    diff = end_val - start_val

    filtered_data.append((gu, int(end_val), int(diff)))



# ===============================
# 4. 카드 Top5 / Bottom5
# ===============================
filtered_data.sort(key=lambda x: x[2], reverse=True)

top5 = filtered_data[:5]
bottom5 = filtered_data[-5:]

selected = top5 + bottom5

cols = st.columns(5)

for i, (gu, val, diff) in enumerate(selected):
    cols[i % 5].metric(
        label=gu,
        value=val,
        delta=diff
    )