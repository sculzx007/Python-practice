import configparser
import urllib.request
import re
import os
from bs4 import BeautifulSoup
from  http.cookiejar import CookieJar

def readconfig(): #读取配置文件
        cf=configparser.ConfigParser()
        cf.read('setting.ini')
        config={'url':cf.get('default','url'),'loginurl':cf.get('default','loginurl'),'username':cf.get('default','username'),'password':cf.get('default','password')}
        return config
        
def get_pic(url):
        os.chdir(new_path)
        soup=open_url(url)
        for each in soup.find_all(file=re.compile('.jpg')):                
                filename=each['file'].split('/')[-1].split('.')[0]+'.jpg'
                headers={}
                headers['Upgrade-Insecure-Requests']='1'
                headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36' 
                req=urllib.request.Request(each['file'],headers=headers)
                try:
                        print('正在获取:-->',filename)
                        img=urllib.request.urlopen(req,timeout=5).read()
                        with open(filename,'wb') as f:
                                f.write(img)
                except:
                        print('超时，获取失败')
def open_url(req):
        try:
                html=opener.open(req,timeout=5).read()
                soup=BeautifulSoup(html,'html.parser')
                return soup
        except:
                print('访问异常！')
        
def main():       
        data={}
        data['fastloginfield']='username'
        data['username']=config['username']
        data['password']=config['password']
        data['quickforward']='yes'
        postdata=urllib.parse.urlencode(data).encode('utf-8')
        headers={}
        headers['Upgrade-Insecure-Requests']='1'
        headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        req=urllib.request.Request(config['loginurl'],postdata,headers=headers)
        if open_url(req):
                for i in range(5):                      
                        url='http://hkbbcc.net/forum-30-%d.html' %i
                        soup=open_url(url)
                        urllist=[]
                        for each in soup.find_all(href=re.compile('thread-'),class_='z'):
                                urllist.append( ''.join([config['url'],each['href']]))
                        for each in urllist:
                              get_pic(each)
cookie=CookieJar()
config=readconfig()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
path = os.getcwd()
new_path = os.path.join(path, 'pic')
if not os.path.exists(new_path):
    os.mkdir(new_path)                      

if __name__=='__main__':
        main()        
        
