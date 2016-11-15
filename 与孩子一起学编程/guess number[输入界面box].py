# coding=utf-8
import random, easygui
secret = random.randint(1, 99) #调用随机数
#变量初始化
guess = 0
tries = 0
easygui.msgbox ("It is a number from 1 to 99. I'll give you 6 tries")
while guess != secret and tries < 6:  #while循环，规定了尝试次数
    guess = easygui. integerbox ("What's youe guess?")
    if not guess: break
    if guess < secret:
        easygui.msgbox (str (guess) + " is too low")
    elif guess > secret:
        easygui.msgbox (str (guess) + " is too high")
    tries = tries + 1   #尝试次数+1
if guess == secret:
    easygui.msgbox("You got it! Found my secret!")
else:
    easygui.msgbox("No more guess! Better luck next time!")
