print('hello world')


import requests


print(requests)



url = 'https://www.baidu.com'

response = requests.get(url=url)

print(response.content)
