
import urllib.request
import re

Error = False

class Ip:
    ip = ''
    dk = 80  #默认80
    lx = 'HTTP'

def open_url(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        page = urllib.request.urlopen(req)
        html = page.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print('发生错误了:',e)
        html = ''
        Errror = True
        return html
    except urllib.error.URLError as e:
        print('发生错误了:',e)
        html = ''
        Error = True
        return html
    else:
        return html

def get_ip(html):
    if Error == False:
        dk = []
        lx = []
        p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
        a = html.find('<td data-title="PORT">')
        b = html.find('</td>',a)
        dk.append(html[a+22:b])
        a = html.find('<td data-title="类型">')
        b = html.find('</td>',a)
        lx.append(html[a+20:b])
        iplist = re.findall(p, html)
        for each in iplist:
            for each_dk in dk:
                for each_lx in lx:
                    ip = Ip()
                    ip.ip = each
                    ip.dk = each_dk
                    ip.lx = each_lx
                    return ip
    else:
        return None

    
if __name__ == '__main__':
    i = 1
    while i<1000:
        url = "http://www.kuaidaili.com/free/inha/"+str(i)
        ipaddrs = Ip()
        ipaddrs = get_ip(open_url(url))
        if Error == False and ipaddrs != None:
            print('IP:'+ipaddrs.ip+'  端口:',str(ipaddrs.dk)+'   协议:'+ipaddrs.lx)
            i+=1
        else:
            Error = False  #发生错误后自恢复

