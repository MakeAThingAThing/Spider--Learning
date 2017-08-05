from urllib import request
from bs4 import BeautifulSoup
from urllib import parse
import pymysql.cursors

#直接请求
#response = request.urlopen('http://123.207.187.243/homepages/')

#获取状态码
#print(response.read().decode("utf-8"))

#携带User-Agent头
"""
req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
"""

#使用POST
"""
req = request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
    ("SearchDate", "2017/05/23"),
    ("SearchTime", "23:00"),
    ("SearchWay", "DepartureInMandarin"),
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36")
resp = request.urlopen(req, data=postData.encode("utf-8"))

print(resp.read().decode("utf-8"))
"""
