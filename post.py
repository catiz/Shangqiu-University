import requests
import time
import json

date = time.strftime("%Y-%m-%d", time.localtime())
url = "http://xg.sqxy.edu.cn/xgh5/openData"
data = {"command":"XGXT","param":'{"cmd":"yqsbFormSave","xh":"2019050500","sbsj":'+date+',"nl":"17","lxfs":"17734718888","jzdq":"411403","jzdq_xxdz":"毛堌堆乡","tw":"36.5","sflx":"0","jcbr":"0","zyzz":"1,","fbrq":"","zyzzms":"","bz":"","bz1":"","wcjtgj":"","wcjtgjxq":"","wcdq":"","wcdqxxdz":"","lkdate":"","fhdate":"","zszt":""}'}
res = requests.post(url=url,data=data)
headers = {'Content-Type': 'application/json'}
if json.loads(res.text)['message'] == "成功":
    requests.post(url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c", headers=headers,data=json.dumps({"text": {"content":""+date+" 报平安提交成功"},"msgtype":"text"}))
if json.loads(res.text)['message'] == "不能重复上报!":
    requests.post(url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c", headers=headers,data=json.dumps({"text": {"content":""+date+" 报平安重复"},"msgtype":"text"}))
else:
    requests.post(url="https://oapi.dingtalk.com/robot/send?access_token=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c", headers=headers,data=json.dumps({"text": {"content":""+date+" 报平安失败"},"msgtype":"text"}))
