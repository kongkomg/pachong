#get请求
import requests

r=requests.get("http://www.baidu.com/")
print(type(r))
print(r.status_code)
print(r.text.encode("utf-8"))
print(r.cookies)

#params用于传递参数
data = {'name':'zhu','age':'22'}
r=requests.get("https://httpbin.org/get",params=data)
print(r.text)

#爬知乎，传入headers
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.5.4000'
}
r=requests.get("http://www.zhihu.com/explore",headers=headers)
print(r.headers)
print(r.status_code)
print(r.cookies)
