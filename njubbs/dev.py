import urllib.request           #get html content
import webbrowser               #open browser to display html
import codecs                   #encode
from bs4 import BeautifulSoup   #parse html
import re                       #regular expression

def main():
    board = 'JobAndWork'
    contents = ['IT']
    html = getURLHtmlContent('http://bbs.nju.edu.cn/bbsdoc?board={0}&type=doc'.format(board))
    #displayHTMLAtBrowser(html)
    soup = BeautifulSoup(html)
    aTagArr = soup.findAll('a', attrs={'href':re.compile('bbscon')})
    for element_a in aTagArr:
        ticketURL = 'http://bbs.nju.edu.cn/' + element_a.get('href')
        print(ticketURL)
        isContentFromTicketURL(ticketURL, contents)                
        
    
    
def getURLHtmlContent(url):
    resp = urllib.request.urlopen(url)
    content = resp.read()
    html = content
    return html

def displayHTMLAtBrowser(html):
    f = codecs.open('hello.html', 'w', 'gbk')
    f.write(html.decode('gbk'))
    f.close()
    webbrowser.open_new_tab('hello.html')

def isContentFromTicketURL(ticketURL, contents):
    html = getURLHtmlContent(ticketURL)
    soup = BeautifulSoup(html)
    if soup.get_text().find(contents[0])!=-1:
        print(soup.get_text())
        return True
    else:
        return False


if __name__=='__main__':
    main()
