import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# elem1 = driver.find_element_by_css_selector("#q")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://piao.damai.cn/138382.html?spm=a2o6e.search.0.0.2b5328df7CB40F")

# test
# driver.get("https://piao.damai.cn/141699.html?spm=a2o6e.search.0.0.10f94d15pF81cd")


def choose(seletor):
    try:
        choice = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor)))
        return choice
    except TimeoutException as e:
        print("Time out!")
        return None
    except Exception:
        print("Not found!")
        return None

# 登录
login = choose("#userLoginInfo > span > a:nth-child(1)")
login.click()
username = choose("#login_email")
username.send_keys("13112355359")
# password = choose("#login_pwd")
# password = driver.find_element_by_id("login_pwd")
# password.click()
# password.send_keys("haobang058")
# subbtn = choose("#subbtn")
# subbtn.click()

time.sleep(5)
while 1:
    if 11 == time.localtime().tm_hour:
        while 1:
            if 18 == time.localtime().tm_min:
                print("开始抢票")
                driver.get("https://piao.damai.cn/138382.html?spm=a2o6e.search.0.0.2b5328df7CB40F")
                price = None
                plus = None
                buybtn = None
                submit = None
                # 点击价格
                while None == price:
                    price = choose("li.itm-oos:nth-child(2)")
                print(price)
                price.click()
                # 数量加1
                while None == plus:
                    plus = choose("a.btn:nth-child(3)")
                plus.click()
                # 立即抢购
                while None == buybtn:
                    buybtn = choose("#btnBuyNow")
                buybtn.click()
                # btnXuanzuo
                # 提交订单ÍÍÍ
                while None == submit:
                    submit = choose("#orderConfirmSubmit")
                submit.click()
                break


time.sleep(10)
# driver.quit()
price("抢票成功")
