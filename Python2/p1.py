"""思路：
不断地抓取服务器发送过来的包（问题出现的时候包会携带信息）
在包中提取出问题信息，自动打开浏览器进行搜索
"""

import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 打开谷歌浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 找到搜索框控件
elem = driver.find_element_by_xpath('//*[@id="kw"]')
# 搜索按键控件
search = driver.find_element_by_xpath('//*[@id="su"]')

def count_num(question, answers):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}
    html = requests.get('https://www.baidu.com/s?wd='+question, timeout=4, headers=header).text
    num = [html.count(answers[0]), html.count(answers[1]), html.count(answers[2])]
    print(num)

# 问题列表，防止不断搜索
questions = []

def auto_search():
    try:
        # 请求网页
        resp = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current', timeout=4).text
        # 字符串转化为json数据
        resp_dict = json.loads(resp)
        # 空包，没信息
        if resp_dict['msg'] == 'no data':
            return None
        else:
            # 有信息
            resp_dict = eval(str(resp))
            # 提取问题信息（已经是json格式）
            question = resp_dict['data']['event']['desc']
            question = question[question.find('.') + 1:question.find('?')]
            if question not in questions:
                # 问题出现的时候是持续出现的，出现过的问题放在列表里，可以只查询一次
                questions.append(question)
                try:
                    print('问题: ')
                    print(question)
                    #自动搜索
                    # 清空搜索框
                    elem.clear()
                    # 输入问题
                    elem.send_keys(question)
                    # 点击搜索
                    search.click()
                    # 提取并输出答案选项
                    answers = eval(resp_dict['data']['event']['options'])
                    print('选项: ')
                    print(answers)
                    count_num(question, answers)
                    count_num(question+answers[0], answers)
                    count_num(question+answers[1], answers)
                    count_num(question+answers[2], answers)
                except:
                    print("Error")
            else:
                return None
    except:
        return None



def main():
    # question = "电视剧《乡村爱情》中，角色“谢大脚”在剧中的本名叫"
    # answers = ['谢红', '谢芳', '谢琳']
    # count_num(question, answers)
    # question = "电视剧《乡村爱情》中，角色“谢大脚”在剧中的本名叫谢红"
    # answers = ['谢红', '谢芳', '谢琳']
    # count_num(question, answers)
    # question = "电视剧《乡村爱情》中，角色“谢大脚”在剧中的本名叫谢芳"
    # answers = ['谢红', '谢芳', '谢琳']
    # count_num(question, answers)
    # question = "电视剧《乡村爱情》中，角色“谢大脚”在剧中的本名叫谢琳"
    # answers = ['谢红', '谢芳', '谢琳']
    # count_num(question, answers)
    print("Start...")
    while True:
        auto_search()

if __name__ == '__main__':
    main()
