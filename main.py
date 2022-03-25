import time
import requests
from selenium import webdriver
import random
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import TimeoutException
import json
import re
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np


def post():
    date = time.strftime("%Y-%m-%d", time.localtime())
    url = "http://xg.sqxy.edu.cn/xgh5/openData"
    data = {"command": "XGXT",
            "param": '{"cmd":"yqsbFormSave","xh":"2019050500","sbsj":' + date + ',"nl":"17","lxfs":"18888888888","jzdq":"411403","jzdq_xxdz":"毛堌堆乡","tw":"36.5","sflx":"0","jcbr":"0","zyzz":"1,","fbrq":"","zyzzms":"","bz":"","bz1":"","wcjtgj":"","wcjtgjxq":"","wcdq":"","wcdqxxdz":"","lkdate":"","fhdate":"","zszt":""}'}
    res = requests.post(url=url, data=data)
    if res.status_code == 200:
        return json.loads(res.text)['message']
    else:
        return "error"


def img():
    bk_img = cv2.imread(r"/www/wwwroot/1647683763900.jpg") # 截图模板图片路径
    fontpath = r"/www/wwwroot/MiSans-Normal.ttf"    # 设置需要显示的字体
    font = ImageFont.truetype(fontpath, 35)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    i = 1
    y = 571
    date = int(time.time())

    while i < 10:
        timeArray = time.localtime(date)
        txt = str(time.strftime("%Y-%m-%d 00:00:0", timeArray))+str(random.randint(0,9))
        draw.text((38, y), txt, font=font, fill=(153, 153, 153))
        y += 203
        i += 1
        date -= 86400

    bk_img = np.array(img_pil)

    cv2.imwrite(r"/www/wwwroot/add_text.jpg", bk_img)# 生成新的截图路径


def browser_initial():
    
    driver_path = '/www/wwwroot/chromedriver' # chromedriver文件路径
    chrome_option = ChromeOptions()
    chrome_option.headless = True
    chrome_option.add_argument('--no-sandbox') #解决DevToolsActivePort文件不存在的报错
    chrome_option.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
    chrome_option.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
 
    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_option)

    browser.get('https://qzone.qq.com/')
    return browser


def log_csdn(browser):
    with open('/www/wwwroot/QQ空间_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.qq.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()  # 刷新网页,cookies才成功


def upload(browser):
    Qid = "605934999" # 群相册所在群QQ号
    time.sleep(1)
    browser.set_page_load_timeout(5)
    try:
        browser.get('https://h5.qzone.qq.com/groupphoto/album?inqq=1&groupId=' + Qid)
    except TimeoutException:  # 捕获timeout异常
        browser.execute_script('window.stop()')  # 执行Javascript来停止页面加载 window.stop()

    html = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/ul').get_attribute('innerHTML')
    pattern = re.compile('<li class=[^>]*>')

    ck = pattern.findall(html)
    date_m = time.strftime("%m", time.localtime())
    date_d = time.strftime("%d", time.localtime())
    pattern2 = re.compile('[' + date_m + '][\u4E00-\u9FA5.][' + date_d + ']+[\u4E00-\u9FA5]+') # 正则获取今日相册地址
    pattern3 = re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{32}')
    aid="null"
    for k in ck:
        if pattern2.search(k) is not None:
            aid = pattern3.search(k).group()
            break
    
    time.sleep(5)
    browser.get('https://h5.qzone.qq.com/groupphoto/album?inqq=1&groupId=' + Qid + '&aid=' + aid)
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/a[5]').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/a/input').send_keys(
        r"/www/wwwroot/add_text.jpg")  # 上传截图文件
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/a[2]').click()
    time.sleep(5)
    browser.quit()


if __name__ == "__main__":
    headers = {'Content-Type': 'application/json'}
    if post() == "成功":
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "报平安提交成功"}, "msgtype": "text"})) # 钉钉机器人通知
        img()
        browser = browser_initial()
        log_csdn(browser)
        upload(browser)
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "上传截图至群相册成功"}, "msgtype": "text"})) # 钉钉机器人通知
    if post() == "不能重复上报!":
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "报平安重复"}, "msgtype": "text"})) # 钉钉机器人通知
    if post() == 'error':
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "报平安出现未知错误"}, "msgtype": "text"})) # 钉钉机器人通知
