import requests
import json

url = 'http://www.weather.com.cn/data/sk/101020100.html'
#url='http://www.dg121.com/index.php/portal/town/index/town/ca'
headers={
'Accept':'*/*',
#'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'d1.weather.com.cn',
'Referer':'http://www.weather.com.cn/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.3636'}

r = requests.get(url, headers = headers,allow_redirects=False)


#js = json.dumps(r.json(),ensure_ascii=False)

print(r.status_code)

print(r.content)

print(r.encoding)
