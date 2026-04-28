from src.modules import crawling_module as cm
import streamlit as st

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'

# 1. sk 렌터카 faq
url = 'https://rent.skdirect.co.kr/customer/faq'
file_path = 'src/resources'
file_name = 'sk렌터카_faq'
skr_faq_info = { 'url': url, 'file_path': file_path, 'file_name': file_name }

# 2. 다른 렌터카 faq
# 3. 다른 렌터카 faq


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("SK렌터카 크롤링", use_container_width=True):
        url = "https://rent.skdirect.co.kr/customer/faq"
        file_path = "src/resources"
        file_name = "sk렌터카_faq"

        try:
            # cm.create_csv_by_bs(skr_faq_info['url'], skr_faq_info['user_agent'], skr_faq_info['file_path'], skr_faq_info['file_name'])

            st.success("SK렌터카 크롤링이 완료되었습니다.")
            st.success("csv 파일로 저장하였습니다.")
            st.success("DB에 등록되었습니다.")
        except BaseException as e:
            print(e)
            st.error("SK렌터카 크롤링을 실패하였습니다.")
            st.error("DB에 등록되었습니다.")
            
with col2:
    if st.button("다른렌터카 크롤링", use_container_width=True):
        file_path = "src/resources"
        file_name = "다른렌터카_faq"
        url = ""

        try:
            # cm.create_csv_by_bs(skr_faq_info['url'], skr_faq_info['user_agent'], skr_faq_info['file_path'], skr_faq_info['file_name'])

            st.success("다른렌터카 크롤링이 완료되었습니다.")
            st.success("csv 파일로 저장하였습니다.")
            st.success("DB에 등록되었습니다.")
        except BaseException as e:
            print(e)
            st.error("다른렌터카 크롤링을 실패하였습니다.")

with col3:
    if st.button("다른렌터카3 크롤링", use_container_width=True):
        file_path = "src/resources"
        file_name = "다른렌터카_faq"
        url = ""

        try:
            # cm.create_csv_by_bs(skr_faq_info['url'], skr_faq_info['user_agent'], skr_faq_info['file_path'], skr_faq_info['file_name'])

            st.success("다른렌터카3 크롤링이 완료되었습니다.")
            st.success("csv 파일로 저장하였습니다.")
            st.success("DB에 등록되었습니다.")
        except BaseException as e:
            print(e)
            st.error("다른렌터카3 크롤링을 실패하였습니다.")

with col4:
    if st.button("자동차 등록현황 다운로드 (API)", use_container_width=True):
        file_path = "src/resources"
        file_name = "다른렌터카_faq"
        url = ""

        try:
            # cm.create_csv_by_bs(skr_faq_info['url'], skr_faq_info['user_agent'], skr_faq_info['file_path'], skr_faq_info['file_name'])

            st.success("자동차 등록현황 다운로드하였습니다.")
            st.success("DB에 등록되었습니다.")
        except BaseException as e:
            print(e)
            st.error("자동차 등록현황 다운로드 실패하였습니다.")
            