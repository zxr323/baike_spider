from urllib import request as urllib2
import http.cookiejar


# urllib2 下载共三种方法
url = "http://www.baidu.com"
print("第一种方法")
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法") # 用request对象做特殊处理，爬虫伪装成浏览器
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)  # 具有了cookie处理能力
response3 = urllib2.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())


