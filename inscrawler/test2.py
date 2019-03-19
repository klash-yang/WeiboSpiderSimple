import requests
import json



url = 'https://apis.yum6.cn/api/5bd44dc94bcfc?token=f07b711396f9a05bc7129c4507fb65c5'


file = open('./data/edcee3000/Bu_N2oRnLtg/image.jpg', 'rb')
# file_params = {'file': ('pic.jpg', file, 'image/jpeg')}
file_params = {'file': ('pic.jpg', file, 'image/jpeg')}

data = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

r = requests.post(
    url=url,
    data=data,
    files=file_params,

)

a = json.loads(r.content)
print(a['data']['url'])