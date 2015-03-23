import urllib.request
import webbrowser
import codecs
from html.parser import HTMLParser

resp = urllib.request.urlopen('http://bbs.nju.edu.cn/bbsdoc?board=JobAndWork&type=doc')
content = resp.read()
html = str(content, 'GBK').encode('gbk')
#html = content

f = codecs.open("hello.html", 'w', "gbk")
f.write(html.decode("gbk"))
f.close()
webbrowser.open_new_tab("hello.html");
