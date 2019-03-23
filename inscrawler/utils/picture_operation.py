import requests
import json
from inscrawler.settings import PHOTO_BED_UPLOAD_URL


def upload_picture(file_address):
    url = PHOTO_BED_UPLOAD_URL
    file_address = '../' + file_address
    file = open(file_address, 'rb')
    file_params = {'file': ('pic.jpg', file, 'image/jpeg')}

    data = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    r = requests.post(
        url=url,
        data=data,
        files=file_params,
    )

    resp = json.loads(r.content)
    # url = resp['data']['url']
    print(resp)
    # return url

upload_picture('data/edcee3000/Bu-gwyLnJjy/image.jpg')
