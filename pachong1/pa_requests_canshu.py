#是否严重网站证书  verify
import requests
#不显示报错信息
from requests.packages import urllib3
urllib3.disable_warnings()
#cert=（。。。）指定证书，加载网址后面
r=requests.get("http://www.12306.cn/",verify=False)
print(r.status_code)

#设置代理  proxies
proxies={
"http":"http://...",
"https":"https://...",
"http":"http://User:password@..."#代理有密码  http://用户名：密码@IP地址
"http":"socks5://User:password@..."#socks5://...  socks代理形式
}
r=requests.get("http://www.12306.cn/",proxies=proxies)

#超时设置 timeout
r=requests.get("http://www.12306.cn/",timeout=1)

#认证才可登陆的网站 auth
from requests.auth import HTTPBasicAuth
r=requests.get("http://www.12306.cn/",auth=('user',‘123’))
