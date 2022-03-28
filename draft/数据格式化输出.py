"""
草稿，练手用
"""
# 数据的格式化输出
# %s 字符串 、 %f 浮点数 （%.2f）保留俩位  、%d 整数
name = input(str("请输入姓名："))

print("我的名字叫%s,请多关关照" % name)

stu_num = 123456
print("你的学号是%d"% stu_num)

price = float(input('APPLE的单价为：'))
weight = float(input("购买的数量为："))
money = price * weight
print('单价为%.2f,重量为%.1f,你需要支付%.2f'%(price,weight,money))





