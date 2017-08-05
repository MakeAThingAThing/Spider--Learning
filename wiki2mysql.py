#抓取wiki

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

# 请求URL并把URL用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
# 使用beautifulSoup去解析
soup = BeautifulSoup(resp, "html.parser")
# 获取所有以/wiki/开头的a标签的herf属性
listUrls = soup.findAll("a", href=re.compile("^/wiki"))
for url in listUrls:
    #过滤以.jpg|JPG结尾的URL
    if not re.search("\.(jpg|JPG)$", url["href"]):
        print(url.get_text(), "<---->", 'https://en.wikipedia.org' + url["href"])
        #获取数据库连接
        connection = pymysql.connect(host='192.168.64.132',
                                     user='root',
                                     password='paSSport',
                                     db='wikiurl',
                                     charset='utf8')
        try:
            #获取会话指针
            with connection.cursor() as cursor:
                #创建sql语句 tip: 这里不是单引号，是反单引号，位于esc键下方
                sql = "insert into `urls` (`urlname`, `urlhref`) values(%s, %s)"

                #执行sql语句
                cursor.execute(sql, (url.get_text(), "https://en.wikipedia.org" + url["href"]))

                #提交
                connection.commit()
        finally:
            connection.close()