import requests


def upload(file_name):
    url = 'http://www.freebuf.com/buf/plugins/ueditor/ueditor/php/imageUp.php&post_id='
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    cookies = {
        '3cb185a485c81b23211eb80b75a406fd': '1524312580',
        'PHPSESSID': 'lrps8el9u799le2agl56hhqlf0'}
    r = requests.post(url, headers=headers, cookies=cookies,
                      files={'upfile': open(file_name, 'rb')}, )

    return r


a = upload('./data/edcee3000/Bu_N2oRnLtg/image.jpg')
print(a)