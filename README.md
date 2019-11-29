# 背景简介

一朋友需要下载网页中大量图片，但是一个个点击下载太麻烦，问如何自动将所有图片下载到本地。一开始想使用python爬虫框架scrapy来做这件事，但是会触发网站反爬机制，比较难解决。后来决定使用selenium自动化测试框架来做这件事情，通过自动化测试框架打开页面，就像人操作浏览器打开是一样的，不会轻易的触发反爬机制。于是我就开始做这个项目。

爬取网页图片包含以下几个方面

- 基于python3的selenium页面解析工具集
- docker一键式部署解决依赖
- django常驻进程脚本开发
- rabbitmq异步任务消费

# 快速使用
1. 本地安装
	- git
	- docker
	- docker-compose
2. 克隆项目
	```
	$ git clone git@github.com:baifei2014/crawl.git
	```
3. 拷贝并命名配置文件
	```
	$ cd crawl
	$ cp env.sample .env
	$ docker-compose up
	```

这时，如果生产者已经准备好，发送消息时，就能执行自动下载图片任务了

# License
MIT
