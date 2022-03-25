# 商丘学院自动报平安

[![Shangqiu University](https://img.shields.io/badge/University-Shangqiu-red)](https://www.sqxy.edu.cn/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![README](https://img.shields.io/badge/README-中文-blue.svg)](README.md)
[![Mozilla Public License](https://img.shields.io/badge/Mozilla%20Public%20License-2.0-orange)](https://www.mozilla.org/en-US/MPL/2.0/)


设置Python脚本每日零点自动执行即可实现自动提交报平安，具体提交JSON需自己前往学生综合服务平台抓取即可
进阶可进行自动生成截图上传值指定群相册，需抓QQ空间cookie，使用selenium实现

## 钉钉提醒
至钉钉机器人的Markdown中的图片需要发送图片URL，所以需要在服务器中安装Web服务并保证图片可以访问，我使用的是Nginx
并且需要讲服务器IP添加至机器人IP白名单内

## 环境
1.建议使用Linux的Centos7系统运行
2.安装Python3.6及以上即可，安装需要的库即可，其中PIL安装pillow即可
3.然后需要安装Chrome浏览器和下载对应的chromedriver版本即可
4.最后添加定时执行Python脚本即可，可使用宝塔面板定时任务和直接安装Nginx创建网站来供钉钉拉去图片

## 注意
此脚本仅供学习
需要保证自身环境处于低风险区下使用的人员学习内容
需要保证自身未出现新型冠状病毒肺炎感染症状的人员学习内容
需要保证未感染新型冠状病毒肺炎的人员学习内容
需要保证自身不是密接已经次密接和时空伴随者和15日内未到达非低风险地区的人员学习内容

### 隐瞒病情、瞒报行程信息(尤其是重点地区旅居史)、隐瞒与确诊病例或者疑似病例有密切接触史的，涉嫌违反《治安管理处罚法》第五十条，处警告或者200元以下罚款；情节严重的，处5日以上10日以下拘留，可以并处500元以下罚款。引起新型冠状病毒传播或者有传播严重危险的，可能涉嫌违反《刑法》第三百三十条，构成妨害传染病防治罪；确诊病人、病原携带者，隐瞒病情、瞒报行程信息，进入公共场所或者乘坐公共交通工具，造成新型冠状病毒传播的，可能涉嫌违反《刑法》第一百一十四条、第一百一十五条，构成以危险方法危害公共安全罪。
