import requests
import json

# file = open('../data/edcee3000/Bu6A4AKHoZt/image.jpg', 'rb')

# https://api.images.ac.cn/?type=multipart\
file = open('../data/pic5.jpg', 'rb')
# file_params = {'file': ('pic.jpg', file, 'image/jpeg')}
file_params = {'file': ('pic.jpg', file, 'image/jpeg')}

data = {
    'ssl': True,
    'Accept': 'application/json, text/javascript, */*; q=0.01',

}

r = requests.post(
    url='https://apis.yum6.cn/api/5bd44dc94bcfc?token=f07b711396f9a05bc7129c4507fb65c5',
    data=data,
    files=file_params,

)

a = json.loads(r.content)
print()
