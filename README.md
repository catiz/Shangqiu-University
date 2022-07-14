# 商丘学院自动报平安

[![Shangqiu University](https://img.shields.io/badge/University-Shangqiu-red)](https://www.sqxy.edu.cn/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![README](https://img.shields.io/badge/README-中文-blue.svg)](README.md)
[![Mozilla Public License](https://img.shields.io/badge/Mozilla%20Public%20License-2.0-orange)](https://www.mozilla.org/en-US/MPL/2.0/)


设置Python脚本每日零点自动执行即可实现自动提交报平安，具体提交JSON需自己前往学生综合服务平台抓取即可

进阶可进行自动生成截图上传值指定群相册，需抓QQ空间cookie，使用selenium实现

## 钉钉提醒
至钉钉机器人的Markdown中的图片需要发送图片URL，所以需要在服务器中安装Web服务并保证图片可以访问，我使用的是Nginx

并且需要服务器IP添加在机器人IP白名单内

## 青龙面板
环境变量

SQ_Number 学号
Phone_Number 联系方式 手机号

默认年龄为18岁，上报地区为商丘学院，体温36.5摄氏度

## 环境
1.建议使用Linux的Centos7系统运行

2.安装Python3.6及以上即可，安装需要的库即可，其中PIL安装pillow即可

3.然后需要安装Chrome浏览器和下载对应的chromedriver版本即可

4.最后添加定时执行Python脚本即可，可使用宝塔面板定时任务和直接安装Nginx创建网站来供钉钉拉去图片
