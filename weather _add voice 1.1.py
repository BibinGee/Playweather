# from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re
import pyttsx3


def voice(engine, date, win, temp, weather):
    print(date)
    print('天气：' + weather)
    print('最低温度：' + temp[5:8])
    print('最高温度：' + temp[1:4])
    print('风级：' + win)
    print('\n')

    engine.say(date)
    engine.say('天气：' + weather)
    if temp[5:8] != '':
        engine.say('最低温度：' + temp[5:8])
    if temp[1:4] != '':
        engine.say('最高温度：' + temp[1:4])
    engine.say('风级小于：' + win[1:4])
    engine.runAndWait()


url = 'http://www.weather.com.cn/weather/101281601.shtml'
# add a headers to simulate as a web browser
headers = ("User-Agent",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/61.0.3163.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

resp = opener.open(url).read()

soup = BeautifulSoup(resp, 'html.parser')

# get current date
tagDate = soup.find('ul', class_="t clearfix")

dates = tagDate.h1.string

# Date:tomorrow
tagTDate = soup.findAll('li', class_="sky skyid lv2")
# Date:3 days later
tagDate = soup.findAll('li', class_="sky skyid lv3")

# get all weather information:
tagAllTem = soup.findAll('p', class_="tem")
tagAllWea = soup.findAll('p', class_="wea")
tagAllWin = soup.findAll('p', class_="win")

# pyttsx module initial:
engine = pyttsx3.init()

# get location
location = soup.find('div', class_='crumbs fl')
text = location.getText()

# now start voicing:
print('以下播报' + text[1:3] + text[6:8] + '未来7天天气情况......')
engine.say('以下播报' + text[1:3] + text[6:8] + '未来7天天气情况')
engine.runAndWait()

# Today
voice(engine, dates, tagAllWin[0].i.string, tagAllTem[0].getText(), tagAllWea[0].string)

# Tomorrow
voice(engine, tagTDate[0].h1.string, tagAllWin[1].i.string, tagAllTem[1].getText(), tagAllWea[1].string)

# 3 days later
for k in range(len(tagDate)):
    if (k != 2):
        voice(engine, tagDate[k].h1.string, tagAllWin[k + 2].i.string, tagAllTem[k + 2].getText(),
              tagAllWea[k + 2].string)
    else:
        voice(engine, tagTDate[1].h1.string, tagAllWin[4].i.string, tagAllTem[4].getText(), tagAllWea[4].string)
        voice(engine, tagDate[k].h1.string, tagAllWin[k + 2].i.string, tagAllTem[k + 2].getText(),
              tagAllWea[k + 2].string)

engine.say('天气播报完毕')
engine.runAndWait()
