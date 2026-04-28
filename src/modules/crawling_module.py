import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def bs_crawling(url:str, user_agent:str)->list:
  """
  beautifulsoup으로 크롤링
  Args:
    url (str): 크롤링할 페이지 url
    user_agent (str): user agent
  Returns:
    questions (list): 질문 목록
  """

  headers = { "User-Agent": user_agent }
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = bs(res.text, "html.parser")

  
  text_list = soup.get_text("\n", strip=True).split("\n")
  questions = []

  for text in text_list:
      if text.startswith("Q."):
          questions.append(text.replace("Q.", "").strip())

  return questions


def create_csv(questions:list, filepath:str, filename:str):
  """
  csv 파일생성
  Args:
    questions (list): 질문목록
    filepath (str): 파일경로
    filename (str): 파일명
  """

  df = pd.DataFrame({
      "no": range(1, len(questions) + 1),
      "question": questions
  })

  df.to_csv(f"{filepath}/{filename}", index=False, encoding="utf-8-sig")


def create_csv_by_bs(url:str, user_agent:str, filepath:str, filename:str):
  """
  beautifulsoup으로 크롤링 후 csv파일 생성
  Args:
    url (str): 크롤링할 페이지 url
    user_agent (str): user_agent
    filepath (str): 파일경로
    filename (str): 파일명
  """

  result_list = bs_crawling(url, user_agent)
  create_csv(result_list, filepath, filename)


def sn_crawling():
  """
  selenium 크롤링 후 출력 (테스트)
  Args:
    url (str): 크롤링할 페이지 url
    user_agent (str): user_agent
    filepath (str): 파일경로
    filename (str): 파일명
  """
  option = webdriver.ChromeOptions()
  option.add_argument("--headless")

  service = Service(executable_path=ChromeDriverManager().install())

  browser = webdriver.Chrome(service=service,options=option)
  browser.maximize_window()

  url = "https://rent.skdirect.co.kr/customer/faq?pageNum=1&tab=&searchWord="
  browser.get(url)


  time.sleep(1) # 지정한 초만큼 일시멈춤
  
  html = browser.page_source
  print(html)

  browser.close()
  print("완료")