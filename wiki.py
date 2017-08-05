#抓取wiki

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
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
