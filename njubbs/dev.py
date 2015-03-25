import urllib.request           #get html content
import webbrowser               #open browser to display html
import codecs                   #encode
from bs4 import BeautifulSoup   #parse html
import re                       #regular expression

def main():
    board = 'JobAndWork'
    contents = ['华为', 'IT', '趋势', 'Trend']
    urlHome = 'http://bbs.nju.edu.cn/bbsdoc?board={0}&type=doc'.format(board)
    pageFrom = 10;
    pageEnd = 500;
    for i in range(pageEnd):
        try:
            print(i)
            html = getURLHtmlContent(urlHome)
            urlHome = getNextPageFromURL(urlHome)
            if(i>pageFrom):
                soup = BeautifulSoup(html)
                aTagArr = soup.findAll('a', attrs={'href':re.compile('bbscon')})
                for element_a in aTagArr:
                    try:
                        ticketURL = 'http://bbs.nju.edu.cn/' + element_a.get('href')
                        if(isContentFromTicketURL(ticketURL, contents)==True):
                            print(ticketURL)
                            print(getCoreContentFromURL(ticketURL))
                    except:
                        print(" exception")
        except:
            print("exception")
        
    
    
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
    text = getCoreContentFromURL(ticketURL)
    for content in contents:
        if text.find(content)!=-1:
            return True
    return False

#get next page's url
def getNextPageFromURL(url):
    html = getURLHtmlContent(url)
    soup = BeautifulSoup(html)
    tag = soup.find(text=re.compile('上一页')).parent
    return 'http://bbs.nju.edu.cn/' + tag['href']

def getCoreContentFromURL(url):
    html = getURLHtmlContent(url)
    soup = BeautifulSoup(html)
    arr = soup.get_text().split('\n')
    narr = []
    for ele in arr:
        if(ele!='' and ele.startswith(':')==False):
            if ele=='--':
                break
            else:
                narr.append(ele)
    return (''.join(narr[4:len(narr)-1]))

def test():
    getURLHtmlContent('http://bbs.nju.edu.cn/bbscon?board=JobAndWork&file=M.1427248873.A&num=11887')

if __name__=='__main__':
    main()
