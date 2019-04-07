# 2019/2/22 第一次学第一节数据结构算法
money = 100
score = 0
for g in range(0,21):
    for m in range(0,34):
        for x in range(0,301):
            score = g*5 + m*3 + float(x)/3
            if score == money and g+m+x ==100:
                print('公鸡 %s 只，母鸡%s只，小鸡%s只'%(g,m,x))
            else:
                pass


# 2019/3/19 第二次学第一节数据结构算法
money = 100
num = 100
# x 公鸡 5元 20只
# y 母鸡 3元 33只
# z 小鸡 0.5元 200只
for x in range(20):
    for y in range(33):
        for z in range(100):
            if x+y+z == num and x*5 + y*3 + z*0.5 == money:
                print("公鸡", x, "母鸡", y, "小鸡", z)