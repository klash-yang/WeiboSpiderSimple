import requests
import imghdr


file = open('../data/edcee3000/Bu6A4AKHoZt/image.jpg', 'rb')
file_params = {'smfile': ('pic.jpg', file, 'image/jpeg')}

data = {
    'ssl': True
}

r = requests.post(
    url='https://sm.ms/api/upload',
    data=data,
    files=file_params,
)

a = r.content
print()