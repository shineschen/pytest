# list列表操作
name_list = []

# 在指定位置添加数据
name_list.insert(0, '草东没有派对')
print(name_list)
name_list.insert(0, '五条人')
print(name_list)

# 在末尾添加数据
name_list.append('新裤子')
print(name_list)

# 将列表添加到列表
text_list1 = [1,2,3]
text_list2 = [4,5,6]
text_list1.extend(text_list2)
print(text_list1)

# 修改指定位置的元素
name_list[0] = '五月天'
print(name_list)

# 删除指定元素
del name_list[2]
print(name_list)

# 删除列表中第一个数据（元素重复时）
name_list.append('五月天')
print(name_list)
name_list.remove('五月天')
print(name_list)

# pop删除
# 不传参数，删除最后一个元素
name_list.pop()
print(name_list)

# 传参数，删除对应的数据
name_list.pop(0)
print(name_list)

# 清除整个列表
name_list.clear()
print(name_list)

# 统计列表元素数量
print(name_list.__len__())

# 统计列表中元素出现的次数
print(name_list.count('五月天'))

# 列表排序
number_list = [8, 9,8, 4, 3, 2, 7]

# 升序
number_list.sort()
print(number_list)

# 降序
number_list.sort(reverse=True)
print(number_list)

# 逆序
number_list.reverse()
print(number_list)

