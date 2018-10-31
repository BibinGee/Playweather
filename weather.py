
#from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://www.weather.com.cn/weather/101281601.shtml'

headers=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

resp = opener.open(url).read()


soup=BeautifulSoup(resp,'html.parser')
#print(soup)



tagDate=soup.find('ul', class_="t clearfix") #get current date
#print(tagDate)

dates=tagDate.h1.string

tagToday=soup.find('p', class_="tem") # get temperature


try:
    temperatureHigh=tagToday.span.string
except AttributeError as e:
    temperatureHigh=tagToday.find_next('p', class_="tem").span.string

temperatureLow=tagToday.i.string

weather=soup.find('p', class_="wea").string

tagWind=soup.find('p',class_="win")
winL=tagWind.i.string

lo = soup.find('div', class_='crumbs fl')
text = lo.getText()
print('Location:'+text[1:3]+text[6:8])

print('今天是：'+dates)
print('风级：'+winL)
print('最低温度：'+temperatureLow)
print('最高温度：'+temperatureHigh)
print('天气：'+weather)
print('\n')

tagTDate = soup.find('li', class_="sky skyid lv2")
tagDate = soup.findAll('li', class_="sky skyid lv3")
tagAllTem=soup.findAll('p', class_="tem")
tagAllWea = soup.findAll('p', class_="wea")
tagAllWin = soup.findAll('p', class_="win")
#print(tagTomrDate.h1.string)

print('明天是：'+tagTDate.h1.string)
print('风级：'+tagAllWin[1].i.string)
print('最低温度：'+tagAllTem[1].i.string)
print('最高温度：'+tagAllTem[1].span.string)
print('天气：'+tagAllWea[1].string)
print('\n')

k = 2
for k  in range(4):
    print(tagDate[k].h1.string)
    print('风级：'+tagAllWin[k].i.string )
    print('最低温度：' + tagAllTem[k].getText()[5:8])
    print('最高温度：' + tagAllTem[k].getText()[1:4])
    print('天气：'+tagAllWea[k].string)
    print('\n')

#tagDate = soup.findAll('li', class_="sky skyid lv3")
#for i in range(5):
#    print(tagDate[i].h1.string)

#print('-----------7 days temperature-------------')
#tagAllTem=soup.findAll('p', class_="tem") 
#for i in range(7):
#    print('High : '+tagAllTem[i].span.string + '℃, Low : '+tagAllTem[i].i.string)

#print('-----------7 days weather-------------')
#tagAllWea = soup.findAll('p', class_="wea")
#for i in range(6):
#    print(tagAllWea[i].string)

#print('-----------7 days wind-------------')
#tagAllWin = soup.findAll('p', class_="win")
#for i in range(6):
#    print(tagAllWin[i].i.string)    
