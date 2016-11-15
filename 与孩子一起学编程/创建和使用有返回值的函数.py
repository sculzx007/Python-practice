# coding=utf-8
"""
def calculateTax (price, tax_rate):
    total = price + (price * tax_rate)
    return total                                      #将结果返回给主程序

#以上语句的作用的是定义函数，计算相应的税额，并返回总的价格

my_price = float(raw_input ("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)                #调用函数并把结果保存在totalPrice中
print "price = ", my_price, "Total price = ",totalPrice

"""

                                                                #拓展
#要求用户输入相应的价格和税额，输出价格及总价

def calculateTax (price, tax_rate):
    total = price + (price * tax_rate)
    return total                                      #将结果返回给主程序

#以上语句的作用的是定义函数，计算相应的税额，并返回总的价格

my_price = float(raw_input ("Enter a price: "))
my_taxrate = float(raw_input("Enter a taxrate: "))
"""
实际上，my_price、 my_taxrate 和 函数内部的 price 及 tax_rate是同一个东西
（my_price对应price；my_taxrate对应tax_rate），只是采用了不同的名字

"""
totalPrice = calculateTax(my_price, my_taxrate)                #调用函数并把结果保存在totalPrice中
print "price = ", my_price, " Total price = ",totalPrice


"""

                                                                #参考答案
def calculateTax(price, tax_rate):                       
    total = price + (price * tax_rate)                   
    return total                          # return the total              

my_price = float(raw_input ("Enter a price: "))          

# Call the function and store the result in totalPrice

totalPrice = calculateTax(my_price, 0.06) 
               
print "price = ", my_price, " Total price = ", totalPrice

"""
