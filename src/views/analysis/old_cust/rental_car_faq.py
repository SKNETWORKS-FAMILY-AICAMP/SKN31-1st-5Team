import streamlit as st
from src.modules import streamlit_module as sm
import pandas as pd

st.header("렌터카 통합 FAQ")
st.set_page_config(layout="wide")
sm.make_space(3)


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["SK렌터카", "롯데렌터카", "현대캐피탈렌터카", "AJ렌터카", "SK렌터카", "제주렌터카", "OK렌터카", "하이렌터카"])
column_config = {
    "question": st.column_config.TextColumn("질문", width="large"),
    "answer": st.column_config.TextColumn("답변", width="large"),
}


with tab1:
    file_path = "src/resources/csv/sk렌터카_faq.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config, height=460)



with tab2:
    file_path = "src/resources/csv/롯데렌터카_faq.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)
    


with tab3:
    file_path = "src/resources/csv/현대캐피탈렌터카_faq.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)


with tab4:
    file_path = "src/resources/csv/sample.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)



with tab5:
    file_path = "src/resources/csv/sample.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)



with tab6:
    file_path = "src/resources/csv/sample.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)



with tab7:
    file_path = "src/resources/csv/sample.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)


with tab8:
    file_path = "src/resources/csv/sample.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    st.dataframe(df, use_container_width=True, column_config=column_config)
    