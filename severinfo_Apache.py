import requests
url = "http://192.168.1.9"
r = requests.get(url)
#获取服务器信息
print(r.headers)
print("服务器采用的技术是：",r.headers['Server'])