class HotDog:
    #首先，先定义 __init__( )方法，这会成为热狗的设置默认属性
    def __init__(self):                         #创建实例并设置默认的属性
        self.cooked_level = 0                #表示热狗烤的时间
        self.cooked_string = "Raw"       #表示热狗的生熟程度
        self.condiments = [ ]                  #表示热狗上的配料，如番茄酱、芥末等

    def __str__(self):
        msg = "hot dog"
        if len (self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg
    
    #以上为输入配料的方法

    def cook(self, time):
        self.cooked_level = self.cooked_level + time            #按时间（time）量增加烤制级别
        if self.cooked_level >8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
            
    #以上为不同烤制等级设置字符串

    def addCondiment(self, condiment):
        self.condiments.append(condiment)               #定义新的add_condiment()的方法

    #下面这部分是为了对上面这部分进行测试
           

myDog = HotDog()                 #创建热狗的一个实例，并检查它的属性
print myDog
print "Cooking hot dog for 4 miniutes..."
myDog.cook(4)
print "Cooking hot dog for 3 miniutes..."
myDog.cook(3)
print myDog
print "What happens if I cook it for 10 more minutes?"
myDog.cook(10)
print myDog
print "Now, I'm going to add some stuff on my hot dog"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print myDog


            
