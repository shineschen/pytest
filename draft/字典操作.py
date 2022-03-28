# 创建一个字典
dic = \
    {
        "name": "小明",
        "age": "35",
        "gender": "man",
        "num": "1001"

    }

print(dic)

# 打印字典中所有的键，返回结果为List
print(dic.keys())

# 打印字典中所有的值，返回的结果为list
print(dic.values())

# items 返回所有key,value的元素为元组的列表
print(dic.items())
# 通过key取value，若key不存在该字典则会报错
print(dic["age"])

# 通过key取value,若key不存在也不会报错,而是返回None
print(dic.get('abcd'))

# 通过key的索引去修改value值
dic['name'] = '小张'
print(dic)

# 删除操作
del dic['age']
print(dic)


for k ,v in dic.items():
    print(k,v)

for k in dic:
    print('%s:%s'%(k,dic[k]))