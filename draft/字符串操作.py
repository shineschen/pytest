

sting = "hello python!"

# for item in sting:
#     print(item)

print(sting[0])

# 切片
print(sting[1:6])


s1 = 'hello,python'

# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())

# 使用title方法将所有单词的首字母转换成大写字母，其他转成小写
print(s1.title())

# 使用upper方法获得所有大写的字符串
print(s1.upper())

# 使用lower方法将所有的字母都转成小写
print(s1.lower())


# 使用find方法,查找字符串所在的位置，返回下标，如果查找的字符串不存在，返回-1
print(s1.find('yt'))
print(s1.find('x'))

# 使用index方法查找字符串所在的位置，返回下标，如果查找的字符串不存在，报错
print(s1.index('yt'))
# print(s1.index('x')) #报错

s = 'hellogoodword'
print(s.find('o'))    #4
print(s.find('o',6))  #7

# 字符串数据判断

# startwith 方法检查字符串是否以指定字符串开头，返回布尔值
print(s1.startswith('he'))

# endswith 方法检查字符串是否以指定字符串结尾，返回布尔值
print(s1.endswith('on'))

# isdigit 方法检查字符串是否由数字构成，返回布尔值
print(s1.isdigit())

# isalpha 方法检查字符是否完全以字母构成,返回布尔值
print(s.isalpha())

# isalnum 方法检查字符传是否以数字和字母构成，返回布尔值
print(s.isalnum())

# 格式化字符串

# 通过center方法以长度20将字串剧中并在两侧填充
print(len(s.center(20, '*')))
print(len(s))

# 通过rjust方法将字符串右侧对齐，并在左侧填充空格
print(s.rjust(20))

# 通过ljust方法将字符串左侧对其，并在右侧填充~~~
print(s.ljust(20,'~'))

