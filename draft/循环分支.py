moneys = int(input('���췢�˶��ٹ���'))
if moneys >=9000 :
    print('���Գ�ȥ����')

elif moneys >=4000 and moneys < 9000:
    print('ֻ��������')

elif moneys <= 3999:
    print('�궿�ӣ�����')

# ����һ����ʼֵ
result = 0
# ������
i = 0
# ѭ����ʼ
while i <=100:
    if i % 2 == 0:
        print(i)

        result += i
    i += 1
print("0~100֮���ż����ͽ�� = %d"% result)