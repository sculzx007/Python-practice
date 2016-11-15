dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40
#以上列出了热狗各部分的卡路里

print "\tDog \tBun \tKetchup\tMustard\tOnions\tCalories"
# \t是水平制表符，注意，为了保持对齐，Ketchup后面不需要加空格

count = 1
for dog in range(2):
    for bun in range(2):
        for ketchup in range(2):
            for mustard in range(2):
                for onion in range(2):
                    total_cal = ((bun*bun_cal) + (dog*dog_cal) + (ketchup*ket_cal)
                                 + (mustard* mus_cal) + (onion*onion_cal))
                    print "#", count, "\t",             #结尾加逗号是为了让其不换行
                    print dog, "\t", bun, "\t",ketchup, "\t",
                    print mustard, "\t", onion,
                    print "\t", total_cal
                    count = count + 1
