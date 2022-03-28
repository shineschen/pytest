# 定义一个元组
info_data = ('张三',1,3.14,1)
print(type(info_data))
info_data1 = tuple('李四，5，7，9')
print(type(info_data1))
# 定义一个空元组
info_data01 = ()
print(type(info_data))

# 在声明元组时，如果元组中的元素只有一个 那么必须在这个值的后面添加一个逗号
info_data03 = (1,)
print(type(info_data03))

# 统计元组中元素出现的次数
print(info_data.count(1))

# 查找元素在元组中的下标
print(info_data03.index(1))

# 将元组转换成列表
info_list = list(info_data03)
print(type(info_list))
