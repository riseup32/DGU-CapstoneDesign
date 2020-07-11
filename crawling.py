import time
import warnings
import re
import pandas as pd
from urllib.parse import quote_plus
from selenium import webdriver


warnings.filterwarnings(action='ignore')


def run():
    # 크롬 드라이버
    baseUrl = "https://www.instagram.com/explore/tags/"
    plusUrl = "검색어"
    url = baseUrl + quote_plus(plusUrl)

    driver = webdriver.Chrome(executable_path="chromedriver_path")
    driver.get(url)
    time.sleep(3)

    # 로그인 클릭
    xpath = '''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'''
    driver.find_element_by_xpath(xpath).click()
    time.sleep(3)

    # 자동 로그인
    element = driver.find_element_by_name("username")
    element.send_keys("user_id")

    element = driver.find_element_by_name("password")
    element.send_keys("user_password")

    xpath = '''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]'''
    driver.find_element_by_xpath(xpath).click()
    time.sleep(7)

    # 크롤링
    xpath = """//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]"""
    driver.find_element_by_xpath(xpath).click()

    tag_list = []
    for i in range(10):
        time.sleep(3)
        try:
            data = driver.find_element_by_css_selector('div.C4VMK')
            tag_raw = data.text
            tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
            tag = ''.join(tags).replace('#', " ").lstrip()
            tag_list.append(tag)

            xpath = """/html/body/div[4]/div[1]/div/div/a[2]"""
            driver.find_element_by_xpath(xpath).click()

        except:
            xpath = """/html/body/div[4]/div[1]/div/div/a[2]"""
            driver.find_element_by_xpath(xpath).click()

    df = pd.DataFrame(tag_list)
    df.to_csv('instagram.csv', index=False)



if __name__ == "__main__":
    run()
