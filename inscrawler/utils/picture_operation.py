import requests
import json
from inscrawler.settings import PHOTO_BED_UPLOAD_URL
import os, sys

def upload_picture(file_address):
    url = PHOTO_BED_UPLOAD_URL
    file = open(file_address, 'rb')
    file_params = {'smfile': ('pic.jpg', file, 'image/jpeg')}

    data = {
        'ssl': True
    }

    r = requests.post(
        url=url,
        data=data,
        files=file_params,
    )

    resp = json.loads(r.content)
    origin_url = str(resp['data']['url'])
    delete_url = str(resp['data']['delete'])
    post_url = origin_url.replace('i.loli.net', 'www.gaoyingzi.com/pic')
    # 删除这个图片所在文件夹
    # file_address = file_address.rstrip('/image.jpg')
    # os.remove(file_address)

    # print(resp)
    return post_url, origin_url, delete_url

# ret_params = upload_picture('../data/edcee3000/Bu-gwyLnJjy/image.jpg')
# print(ret_params)