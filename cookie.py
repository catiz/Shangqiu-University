from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import json
import re
import requests

if __name__ == '__main__':
    driver_path = '/root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
    headers = {'Content-Type': 'application/json'}


    driver = webdriver.PhantomJS(executable_path=driver_path)

    driver.get('https://i.qq.com')
    driver.switch_to_frame("login_frame")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[9]/a[1]").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[1]/div/input").send_keys("2904306586") # QQ号
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[2]/div[1]/input").send_keys("********") # QQ密码

    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[2]/div[1]/input").send_keys(Keys.ENTER)
    time.sleep(1)
    
    
    times = int(time.time())
    driver.save_screenshot('/www/wwwroot/image/image/'+str(times)+'.png')
    requests.post(
        url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
        headers=headers, data=json.dumps({"markdown": {"title":"登录QQ","text": "#### 登录QQ ####\n![screenshot](http://81.69.97.199/image/"+str(times)+".png)\n"}, "msgtype": "markdown"}))
    time.sleep(30)
    # 通常情况下在服务器会需要扫码登录，讲输入密码登录后的截图发送到钉钉查看，如果需要扫码就扫码登录，如果已经登录成功，30秒后即可保存cookie
    
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('/www/wwwroot/QQ空间_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
    requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "cookies保存成功！"}, "msgtype": "text"}))
    driver.close()
