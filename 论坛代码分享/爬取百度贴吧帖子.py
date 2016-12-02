import requests
import re
import os

# 创建存放目录
path = os.getcwd()
new_path = os.path.join(path, 'BDTB')
if not os.path.exists(new_path):
    os.mkdir(new_path)
# 处理页面标签类
class Tool():
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()

# 百度贴吧爬虫类
class BDTB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseURL, seeLZ, floorTag):
        self.baseURL =baseURL
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = "百度贴吧"
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

    # 传入页码，获取页面源码
    def getPage(self,pageNum):
        try:
            url = self.baseURL +self.seeLZ +'&pn='+ str(pageNum)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
            response = requests.get(url,headers)
            # 返回UTF-8格式编码内容
            html = response.text
            return html
            # 无法连接，报错
        except requests.HTTPError as e:
            if hasattr(e, 'code'):
                print("连接贴吧失败,HTTP状态码错误", e.code)
            elif hasattr(e, 'reason'):
                print("连接贴吧失败，错误原因", e.reason)

    # 获取帖子标题
    def getTitle(self,html):
        # 得到标题的正则表达式
        pattern = re.compile('<h\d\sclass="core_title_txt.*?"\stitle="(.*?)"')
        result = re.search(pattern, html)
        if result:
            # 如果存在，则返回标题
            return result.group(1).strip()
        else:
            print('没有标题')
            return None

    # 获取帖子一共多少页
    def getPageNum(self,html):
        # 获取帖子页数的正则表达式
        pattern = re.compile('<span class="red">(\d+)</span>')
        page = pattern.search(html)
        if page:
            return page.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容，传入页面内容
    def getContent(self,html):
        # 匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_\d+"\sclass=".*?">\s+(.*?)</div>')
        items = re.findall(pattern, html)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时前后加入换行符
            content = '\n'+self.tool.replace(item)+'\n'
            contents.append(content)
        return contents

    def setFileTitle(self,title):
        os.chdir(new_path)
        # 如果标题不为None，即成功获取到标题
        if title is not None:
            self.file = open(title +".txt","w")
        else:
            self.file = open(self.defaultTitle + ".txt", "w")

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + str(
                    self.floor) + "-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print("URL已失效，请重试")
            return
        try:
            print("该帖子共有" + str(pageNum) + "页")
            for i in range(1, int(pageNum) + 1):
                print("正在写入第" + str(i) + "页数据")
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        # 出现写入异常
        except IOError as e:
            print("写入异常，原因")+ e.message
        finally:
            print("写入任务完成")
        

print("请输入帖子代号(例如：4868720039)")
baseURL = 'http://tieba.baidu.com/p/' + str(input(u'http://tieba.baidu.com/p/'))
seeLZ = input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()
