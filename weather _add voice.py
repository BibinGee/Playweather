
#from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re
import pyttsx3

def voice(engine,date, win, temp, weather):
    print(date)
    print('风级：' + win)
    print('最低温度：' + temp[5:8])
    print('最高温度：' + temp[1:4])
    print('天气：' + weather)
    print('\n')
        
    engine.say( date)
    engine.say('风级小于：' + win[1:4])
    engine.say('最低温度：' + temp[5:8])
    engine.say('最高温度：' + temp[1:4])
    engine.say('天气：' + weather)
    engine.runAndWait()
    
url = 'http://www.weather.com.cn/weather/101281601.shtml'

headers=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#opener.addheaders = headers
resp = opener.open(url).read()
#resp=urlopen('http://www.weather.com.cn/weather/101281601.shtml')

soup=BeautifulSoup(resp,'html.parser')
#print(soup)

tagDate=soup.find('ul', class_="t clearfix") 
#print(tagDate)

dates=tagDate.h1.string
##
##tagToday=soup.find('p', class_="tem") 
##
##
##try:
##    temperatureHigh=tagToday.span.string
##except AttributeError as e:
##    temperatureHigh=tagToday.find_next('p', class_="tem").span.string
##
##temperatureLow=tagToday.i.string
##
##weather=soup.find('p', class_="wea").string
##
##tagWind=soup.find('p',class_="win")
##winL=tagWind.i.string


tagTDate = soup.findAll('li', class_="sky skyid lv2")

tagDate = soup.findAll('li', class_="sky skyid lv3")
tagAllTem=soup.findAll('p', class_="tem")
##print(tagAllTem)

tagAllWea = soup.findAll('p', class_="wea")
tagAllWin = soup.findAll('p', class_="win")
#print(tagTomrDate.h1.string)

engine = pyttsx3.init()

location = soup.find('div', class_='crumbs fl')
text = location.getText()
##print(text[1:3]+text[6:8])

print('以下播报'+text[1:3]+text[6:8]+'未来7天天气情况')
engine.say('以下播报'+text[1:3]+text[6:8]+'未来7天天气情况')
engine.runAndWait()


voice(engine, dates,tagAllWin[0].i.string,tagAllTem[0].getText(),tagAllWea[0].string)
##print('今天是：' + dates)
##print('风级：' + winL)
##print('最低温度：' + tagAllTem[0].getText()[5:8])
##print('最高温度：' + tagAllTem[0].getText()[1:4])
###print('最低温度：' + tagAllTem[0].i.string)
####print('最高温度：' + tagAllTem[0].span.string)
##print('天气：' + weather)
##print('\n')

##engine.say(dates)
##engine.say('风级小于' + winL[1:4])
##engine.say('最低温度' + tagAllTem[0].getText()[5:8])
##engine.say('最高温度' + tagAllTem[0].getText()[1:4])
##engine.say('天气：' + weather)
##engine.runAndWait()


voice(engine,tagTDate[0].h1.string,  tagAllWin[1].i.string, tagAllTem[1].getText(),tagAllWea[1].string)
##print(tagTDate[0].h1.string)
##print('风级：' + tagAllWin[1].i.string)
##print('最低温度：' + tagAllTem[1].getText()[5:8])
##print('最高温度：' + tagAllTem[1].getText()[1:4])
##print('天气：' + tagAllWea[1].string)
##print('\n')

##engine.say('明天是' + tagTDate[0].h1.string[0:4])
##engine.say('风级小于' + tagAllWin[1].i.string[1:4])
##engine.say('最低温度' + tagAllTem[1].getText()[5:8])
##engine.say('最高温度' + tagAllTem[1].getText()[1:4])
##engine.say('天气' + tagAllWea[1].string)
##engine.runAndWait()

for k in range(len(tagDate)):
    if(k != 2):
        voice(engine, tagDate[k].h1.string,  tagAllWin[k+2].i.string, tagAllTem[k+2].getText(),tagAllWea[k+2].string)
    else:
        voice(engine, tagTDate[1].h1.string,  tagAllWin[4].i.string, tagAllTem[4].getText(),tagAllWea[4].string)
        voice(engine, tagDate[k].h1.string,  tagAllWin[k+2].i.string, tagAllTem[k+2].getText(),tagAllWea[k+2].string)
##for k in range(len(tagDate)):
##    if(k!=2):
##        print(tagDate[k].h1.string)
##        print('风级：' + tagAllWin[k+2].i.string )
##        print('最低温度：' + tagAllTem[k+2].getText()[5:8])
##        print('最高温度：' + tagAllTem[k+2].getText()[1:4])
##    #    print('最低温度：' + tagAllTem[k].i.string)
##    #    print('最高温度：' + tagAllTem[k].span.string)        
##        print('天气：' + tagAllWea[k+2].string)
##        print('\n')
##        engine.say(tagDate[k].h1.string)
##        engine.say('风级小于'+tagAllWin[k+2].i.string[1:4])
##        engine.say('最低温度' + tagAllTem[k+2].getText()[5:8])
##        engine.say('最高温度' + tagAllTem[k+2].getText()[1:4])
##    ##    engine.say('最低温度'+tagAllTem[k].i.string)
##    ##    engine.say('最高温度'+tagAllTem[k].span.string)
##        engine.say('天气' + tagAllWea[k+2].string)
##        engine.runAndWait()
##    else:
##        print(tagTDate[1].h1.string)
##        print('风级：' + tagAllWin[4].i.string)
##        print('最低温度：' + tagAllTem[4].getText()[5:8])
##        print('最高温度：' + tagAllTem[4].getText()[1:4])
##        print('天气：' + tagAllWea[4].string)
##        print('\n')
##
##        engine.say(tagTDate[1].h1.string[0:4])
##        engine.say('风级小于' + tagAllWin[4].i.string[1:4])
##        engine.say('最低温度' + tagAllTem[4].getText()[5:8])
##        engine.say('最高温度' + tagAllTem[4].getText()[1:4])
##        engine.say('天气' + tagAllWea[4].string)
##        engine.runAndWait()
##            
##        print(tagDate[k].h1.string)
##        print('风级：' + tagAllWin[k+2].i.string )
##        print('最低温度：' + tagAllTem[k+2].getText()[5:8])
##        print('最高温度：' + tagAllTem[k+2].getText()[1:4])      
##        print('天气：' + tagAllWea[k+2].string)
##        print('\n')
##        engine.say(tagDate[k].h1.string)
##        engine.say('风级小于'+tagAllWin[k+2].i.string[1:4])
##        engine.say('最低温度' + tagAllTem[k+2].getText()[5:8])
##        engine.say('最高温度' + tagAllTem[k+2].getText()[1:4])
##        engine.say('天气' + tagAllWea[k+2].string)
##        engine.runAndWait()       
    
