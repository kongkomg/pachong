#爬图片，content获取二进制代码
import requests
r=requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")
with open('D:/pythonku/1.gif','wb')as f:
    #二进制流输出 content
    f.write(r.content)
    f.close()
