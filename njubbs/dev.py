import urllib.request           #get html content
import webbrowser               #open browser to display html
import codecs                   #encode
from bs4 import BeautifulSoup   #parse html
import re                       #regular expression

def main():
    board = "JobAndWork"
    html = getURLHtmlContent('http://bbs.nju.edu.cn/bbsdoc?board={0}&type=doc'.format(board))
    #displayHTMLAtBrowser(html)
    soup = BeautifulSoup(html)
    print(soup.findAll("a", attrs={"href":re.compile("bbscon")}))
    
    
def getURLHtmlContent(url):
    resp = urllib.request.urlopen(url)
    content = resp.read()
    html = str(content, 'GBK').encode('gbk')
    return html

def displayHTMLAtBrowser(html):
    f = codecs.open("hello.html", 'w', "gbk")
    f.write(html.decode("gbk"))
    f.close()
    webbrowser.open_new_tab("hello.html")


if __name__=="__main__":
    main()
