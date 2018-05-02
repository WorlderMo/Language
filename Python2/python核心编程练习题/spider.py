#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-20 10:08:24
# @Author  : mohailang (1198534595@qq.com)


# 爬虫是请求网站并提取数据的自动化程序
# 爬虫基本流程：
# 1.发起请求：通过 HTTP 库向目标站点发起请求，即发送一个Request,请求可以包含额外的 headers 等信息，等待服务器响应
# 2.获取响应内容：如果服务器正常响应，会得到一个 Response,Response 的内容便是所要获取的页面内容，类型可能有 HTML,Json,二进制数据(如图片视频)等类型
# 3.解析内容：得到的内容可能是 HTML，可以用正则表达式、网页解析库进行解析。可能是 Json，可以直接换为 Json 对象解析。可能是二进制数据，可以做保存或者进一步的处理
# 4.保存数据：保存形式多样，可以存为文本，也可以保存至数据库，或者保存特定格式的文件
#
# Request和 Response:
# (1)浏览器就发送信息给该网址所在的服务器，这个过程叫做 HTTP Request
# (2)服务器收到浏览器发送的信息后，能够根据浏览器发送的内容做相应的处理，然后把消息回传给浏览器，这个过程叫做 HTTP Response
# (3)浏览器收到服务器的 Response 信息后，会对消息进行相应处理，然后展示
#
# Resquest 包含什么：
# 1.请求方式：主要有 get、post两种类型，另外还有 HEAD、PUT、DELETE、OPTIONS 等
# 2.请求 URL：URL 全称统一资源定位符，如一个网页文档、一张图片、一个视频等都可以用 URL 来唯一确定
# 3.请求头：包含请求时的头部信息，如 User-Agent、Host、Cookie 等信息
# 4.请求体：请求时格外携带的数据如表单提交时的表单数据
#
# Response 包含什么：
# 1.响应状态：有多种响应状态，如200代表成功，301跳转，404找不到页面，502服务器错误
# 2.响应头：如内容类型。内容长度、服务器信息、设置 Cookie 等等
# 3.响应体：最主要的部分，包含了请求资源的内容，如网页 HTML、图片、二进制数据等
#
# 解析方式：直接处理、Json解析、正则表达式、BeautifulSoup解析库、PyQuery解析库、XPath解析库
#
# 怎么解决JavaScript 渲染的问题：
# 分析Ajax 请求、Selenium/WebDriver、Splash、PyV8、Ghost.py
#
# 怎样保存数据：
# 1.文本：纯文本、Json、XML 等
# 2.非关系型数据库：如 MongoDB、Redis等Key-Values 形式存储
# 3.关系型数据库：如 MySQL、Oracle、SQL Server 等具有结构化表结构形式存储
# 4.二进制文件：如图片、视频、音频等等直接保存成特定格式即可
#
# 什么是 Urllib:
# Python 内置的 HTTP 请求库
# urllib. Request 请求模块
# urllib. Error 异常处理模块
# urllib. Parse url 解析模块
# urlib. Robotparser robots. Txt 解析模块
