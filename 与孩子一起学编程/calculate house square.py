# coding=utf-8
#输入长度
length = float(raw_input("Enter length of your house(units: meter): "))
#输入宽度
width = float(raw_input("Enter width of your house(units: meter): "))
square = length * width  #计算房子的面积
carpetsquare = 2 #一块地毯的面积
amountofcarpet = float(square/carpetsquare) #需要地毯的数量
carpetprice = float(raw_input("Enter price of carpet(units: RMB): "))  #地毯单价
totalprice = float(carpetprice*amountofcarpet)  # 地毯总价格
print "square = ", square, " m^2"   #输出房子的面积
print "Need ", amountofcarpet, " m^2 carpet"      #输出所需地毯的面积
print "Need", totalprice, " ( RMB) "      #输出地毯
