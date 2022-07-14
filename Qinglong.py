# -*- coding: UTF-8 -*-
import requests
import time
import json
import os

if __name__ == '__main__':
    date = time.strftime("%Y-%m-%d", time.localtime())
    number = str(os.environ["SQ_Number"])
    phone_number = str(os.environ['Phone_Number'])
    url = "http://xg.sqxy.edu.cn/xgh5/openData"
    data = {"command": "XGXT",
            "param": '{"cmd":"yqsbFormSave","xh":"' + number + '","sbsj":' + date + ',"nl":"18","lxfs":"' + phone_number + '",'
                                                                                '"jzdq":"411402","jzdq_xxdz":"商丘学院",'
                                                                                '"tw":"36.5","sflx":"0","jcbr":"0",'
                                                                                '"zyzz":"1,","fbrq":"","zyzzms":"",'
                                                                                '"bz":"","bz1":"","wcjtgj":"",'
                                                                                '"wcjtgjxq":"","wcdq":"","wcdqxxdz":"",'
                                                                                '"lkdate":"","fhdate":"","zszt":""}'}
    res = requests.post(url=url, data=data)

    headers = {'Content-Type': 'application/json'}
    if json.loads(res.text)['message'] == "成功":
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token"
                "=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "" + date + " 报平安提交成功"}, "msgtype": "text"}))
    if json.loads(res.text)['message'] == "不能重复上报!":
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token"
                "=444c407643bc23a82697d813a2fd4965e773ff617c89352fb17b5ff4fdc85d2c",
            headers=headers, data=json.dumps({"text": {"content": "" + date + " 报平安重复"}, "msgtype": "text"}))

    print("提交成功")
