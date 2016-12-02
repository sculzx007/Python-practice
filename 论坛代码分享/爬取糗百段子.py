import urllib.request
import urllib.error
import re


__author__ = 'hhj'


# 糗事百科类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.agent}
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建请求的request
            request = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib.request.urlopen(request)
            # 将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print("连接糗事百科失败,HTTP状态码错误:", e.code)
            if hasattr(e, "reason"):
                print("连接糗事百科失败,错误原因:", e.reason)
                return None

    # 传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败....")
            return None
        pattern = re.compile(r'''<a href="/users/.*?/" target="_blank" title="(.*?)">.*?<div class="content">\s+<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<span class="cmt-name">(.*?)</span>\s+<div class="main-text">(.*?)<''', re.S)
        items = re.findall(pattern, pageCode)
        # 用来存储每页的段子们
        pageStories = []
        # 遍历正则表达式匹配的信息
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            # item[0]是一个段子的发布者, item[1]是内容, item[2]是人气热度, item[3]是神评人, item[4]是神评内容
            pageStories.append([item[0].strip(), text.strip(), item[2].strip(), item[3].strip(), item[4].strip()])

        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                # 将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    # 获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            # 等待用户输入
            m = input('输入指令(回车=加载，Q=退出)：')
            # 每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            # 如果输入Q则程序结束
            if m == "Q":
                self.enable = False
                return
            print("第%d页\t发布人:%s\n发布内容:%s\t   赞:%s\n神评者:%s\t神评内容:%s\n" % (page, story[0], story[1], story[2], story[3], story[4]))

    # 开始方法
    def start(self):
        print("正在读取糗事百科,按回车查看新段子，Q退出")
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()
