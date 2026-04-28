import streamlit as st


def run():
    """
    스트림릿 시작 (네비게이션 생성)
    """

    create_navigation()


def create_navigation():
    """
    네비게이션 생성 및 페이지 시작
    """

    menu_info = {
        "기존 고객 분석": [
            st.Page("src/views/analysis/old_cust/rental_car_faq.py", title="렌터카 통합 FAQ"),
        ],
        "잠재 고객 분석": [
            st.Page("src/views/analysis/new_cust/car_reg.py", title="자동차 등록 현황"),
            st.Page("src/views/analysis/new_cust/car_acc.py", title="자동차 사고 현황"),

            # st.Page("src/views/analysis/new_cust/car_acc.py", title="나이 지역 현황 분석"),
            # st.Page("src/views/analysis/new_cust/car_acc.py", title="자동차 사고 현황 분석"),
            # st.Page("src/views/analysis/new_cust/car_acc.py", title="자동차 사고 현황 분석"),
            # st.Page("src/views/analysis/new_cust/car_acc.py", title="자동차 사고 현황 분석"),
            # st.Page("src/views/analysis/new_cust/car_acc.py", title="자동차 사고 현황 분석"),
        ],
        "시스템 관리": [
            st.Page("src/views/sys_mg/crawling_mg.py", title="웹크롤링"),
        ],
    }

    pg = st.navigation(menu_info)
    pg.run()


def make_space(n:int):
    """
    간격 주기
    Args:
        n (int): 간격 횟수
    """

    for i in range(n):
        st.write("")