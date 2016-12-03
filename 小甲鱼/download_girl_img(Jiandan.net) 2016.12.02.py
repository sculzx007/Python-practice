import urllib.request
import os
import ssl



def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    
    return html

    
# 获取网页页面地址
def get_page(url):
    
    html = url_open(url).decode('utf-8')

# 获取图片的编号
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]
    

# 获取图片的地址
def find_img_url(url):
    html = url_open(url).decode('utf-8')
    img_url = []

    a = html.find('img src=')
    b = html.find('.jpg', a, a+255)  # 网址一般不是超过255位

# 如果找不到'img src='字段，则a会返回-1，否则不为-1

    while a != -1:
        
    # 如果找不到jpg文件，则b会返回-1，找到则不为-1
        if b != -1:
            img_url.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=', b)

    for each in img_url:
        print(each)

# 保存图片
def save_img(folder, img_url):
    for each in img_url:
        file_name = each.split('/')[-1]

        with open(file_name, 'wb') as f:
            img = url_open(each)
            f.write(img)


# os模块的方法可见网页： http://bbs.fishc.com/forum.php?mod=viewthread&tid=45512&ctid=198

# 下载图片的主函数
def download_girl_img(folder = '煎蛋网', pages = 10):
    # mkdir的作用是创建文件夹
    os.mkdir(folder)
    
    # chdir 改变工作目录
    os.chdir(folder)

    url = 'https://jandan.net/ooxx/'

    ssl._create_default_https_context = ssl._create_unverified_context

    page_num = int(get_page(url))

    for i in range(pages):
        
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'

        img_url = find_img_url(page_url)
        
        save_img(folder, img_url)

if __name__ == '__main__':
    download_girl_img()
