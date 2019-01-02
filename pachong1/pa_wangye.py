#爬豆瓣读书top205，存为TXT
with open('D:\pythonku\doushu.txt','w',encoding='utf-8') as f:
    import requests
    from lxml import etree
    import time

    for a in range(1):
        url = 'https://book.douban.com/top250?start=25'
        data = requests.get(url).text

        s=etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/div/table')

        for div in file:
            ming = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
            numr = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
            pignjia = div.xpath('./tr/td[2]/p[2]/span/text()')[0]

            f.write("{} {} {} {}\n".format(ming,numr,"评价：",pignjia))
