import io

import sys

import requests

data = [
    "?keyword=AM General",
    "?keyword=Acura",
    "?keyword=Alfa Romeo",
    "?keyword=Aston Martin",
    "?keyword=Audi",
    "?keyword=BMW",
    "?keyword=Bentley",
    "?keyword=Buick",
    "?keyword=Cadillac",
    "?keyword=Chevrolet",
    "?keyword=Chrysler",
    "?keyword=Datsun",
    "?keyword=DeLorean",
    "?keyword=Dodge",
    "?keyword=Eagle",
    "?keyword=Ferrari",
    "?keyword=Fiat",
    "?keyword=Fisker",
    "?keyword=Ford",
    "?keyword=GMC",
    "?keyword=Genesis",
    "?keyword=Geo",
    "?keyword=Honda",
    "?keyword=Hummer",
    "?keyword=Hyundai",
    "?keyword=Infiniti",
    "?keyword=Isuzu",
    "?keyword=Jaguar",
    "?keyword=Jeep",
    "?keyword=Karma",
    "?keyword=Kia",
    "?keyword=Lada",
    "?keyword=Lamborghini",
    "?keyword=Land Rover",
    "?keyword=Lexus",
    "?keyword=Lincoln",
    "?keyword=Lotus",
    "?keyword=Maserati",
    "?keyword=Maybach",
    "?keyword=Mazda",
    "?keyword=McLaren",
    "?keyword=Mercedes-Benz",
    "?keyword=Mercury",
    "?keyword=Mini",
    "?keyword=Mitsubishi",
    "?keyword=Mobility Ventures",
    "?keyword=Nissan",
    "?keyword=Oldsmobile",
    "?keyword=Plymouth",
    "?keyword=Pontiac",
    "?keyword=Porsche",
    "?keyword=Ram",
    "?keyword=Rolls Royce",
    "?keyword=Saab",
    "?keyword=Saturn",
    "?keyword=Scion",
    "?keyword=Smart",
    "?keyword=Subaru",
    "?keyword=Suzuki",
    "?keyword=TVR",
    "?keyword=Tesla",
    "?keyword=Toyota",
    "?keyword=VPG",
    "?keyword=Volkswagen",
    "?keyword=Volvo",

    "?keyword=Black",
    "?keyword=Silver",
    "?keyword=Grey",
    "?keyword=White",
    "?keyword=Red",
    "?keyword=Gold",
    "?keyword=Beige",
    "?keyword=Champagne",
    "?keyword=Blue",
    "?keyword=Brown",
    "?keyword=Purple",
    "?keyword=Green",
    "?keyword=Pink",
    "?keyword=Yellow",
    "?keyword=Orange"
]
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')
for sec_data in data:

    url = "http://us.api.wayii.com/vehicle/keyword/search" + sec_data + "&pageNum=1&pageSize=50&location=104.0677&location=30.53519"
    handler = {"User-Agent": "Wayii/2.0.1 (iPhone; iOS 14.8; Scale/3.00)", "Accept-Language": "en;q=1, en-CN;q=0.9",
               "TOKEN": "0954dc0bf4a744a296dbfe7e75eee891"}
    re = requests

    rep = re.get(url=url, headers=handler)
    rep_data = rep.json()
    print(rep_data)
    # print(sec_data)
    print("________________________________")
    nub = (rep_data['data']['total'])

    if nub == 0:
        print('无匹配结果的关键字为：', sec_data)

    else:
        print(sec_data, '已搜索成功，共搜索到：', nub, '条结果')
