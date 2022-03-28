moneys = int(input('今天发了多少工资'))
if moneys >=9000 :
    print('可以出去浪了')

elif moneys >=4000 and moneys < 9000:
    print('只够还花呗')

elif moneys <= 3999:
    print('完犊子，吃土')

# 定义一个初始值
result = 0
# 计数器
i = 0
# 循环开始
while i <=100:
    if i % 2 == 0:
        print(i)

        result += i
    i += 1
print("0~100之间的偶数求和结果 = %d"% result)