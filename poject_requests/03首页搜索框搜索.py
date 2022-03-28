import io

import requests
import sys
data = [
"AM General",
"Acura",
"Alfa Romeo",
"Aston Martin",
"Audi",
"BMW",
"Bentley",
"Buick",
"Cadillac",
"Chevrolet",
"Chrysler",
"Datsun",
"DeLorean",
"Dodge",
"Eagle",
"Ferrari",
"Fiat",
"Fisker",
"Ford",
"GMC",
"Genesis",
"Geo",
"Honda",
"Hummer",
"Hyundai",
"Infiniti",
"Isuzu",
"Jaguar",
"Jeep",
"Karma",
"Kia",
"Lada",
"Lamborghini",
"Land Rover",
"Lexus",
"Lincoln",
"Lotus",
"Maserati",
"Maybach",
"Mazda",
"McLaren",
"Mercedes-Benz",
"Mercury",
"Mini",
"Mitsubishi",
"Mobility Ventures",
"Nissan",
"Oldsmobile",
"Plymouth",
"Pontiac",
"Porsche",
"Ram",
"Rolls-Royce",
"Saab",
"Saturn",
"Scion",
"Smart",
"Subaru",
"Suzuki",
"TVR",
"Tesla",
"Toyota",
"VPG",
"Volkswagen",
"Volvo"
]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')   #改变标准输出的默认编码
for sec_data in data:

    url = "http://us.api.wayii.com/user/search"+"?keyword="+sec_data+"&pageNum=1&pageSize=10&location=104.0677&location=30.53519"
    handler = {"TOKEN":"0954dc0bf4a744a296dbfe7e75eee891"}
    re = requests

    rep = re.get(url=url, headers=handler)
    rep_data = rep.json()
    print(rep_data)
    # print(sec_data)
    print("________________________________")
    nub = (rep_data['data']['total'])
    nub_loc = (rep_data['data']['records'])
    for i in nub_loc:
        if 'distance' in i:
            distance = []
            distance = i['distance']


    if nub == 0:
        print('无匹配结果的品牌为：', sec_data)

    else:
        print(sec_data, '该品牌已搜索成功，共搜索到：', nub, '条结果','距离为：',distance)



