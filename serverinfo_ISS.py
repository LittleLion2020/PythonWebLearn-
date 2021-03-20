import requests
url = "http://192.168.1.9"
r = requests.get(url)
#获取IIS服务器信息
print(r.headers)
print("服务器中间件：",r.headers['Server'])
try:
	print("服务器脚本语言：",r.headers['X-Powered-By'])
except:
	print("Warning: It may not IIS")
