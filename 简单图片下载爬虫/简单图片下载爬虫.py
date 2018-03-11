#下载小黄人照片
import requests

keyword = input("Input key word: ")

url=u"http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+keyword+"&ct=201326592&lm=-1&v=flip"
webdata=requests.get(url)
webdata2=str(webdata.content,encoding="utf8")

#
import re
pic_url = re.findall('"objURL":"(.*?)",',webdata2,re.S)

i = 0
for each in pic_url:
    print(each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue

    string = u'D:\\Users\\dongyuehu\\Documents\\python 练习\\各种爬虫\\简单图片下载爬虫\\pic\\'+str(i) + u'.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

