import requests
import json

# file = open('../data/edcee3000/Bu6A4AKHoZt/image.jpg', 'rb')

# https://api.images.ac.cn/?type=multipart

file = open('../data/pic5.jpg', 'rb')
# file_params = {'file': ('pic.jpg', file, 'image/jpeg')}
file_params = {'file': ('pic.jpg', file, 'image/jpeg')}

data = {
    'ssl': True,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Origin': 'https://images.ac.cn',
    # 'Referer': 'https://images.ac.cn/',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2864.400',
    # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryoPacKT2v8cBF80am'
}

r = requests.post(
    url='https://apis.yum6.cn/api/5bd44dc94bcfc?token=f07b711396f9a05bc7129c4507fb65c5',
    data=data,
    files=file_params,

)

a = json.loads(r.content)
print()
