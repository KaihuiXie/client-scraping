import requests
import http.client
import urllib
from urllib.parse import quote

# 请求头部分
payload = ''

# 获取商品数据参数
conn = http.client.HTTPSConnection("data.p4psearch.1688.com")
headers = {
    'Referer': 'https://p4psearch.1688.com/',
    'Cookie': "记得填cookie",
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Accept': '*/*',
    'Host': 'data.p4psearch.1688.com',
    'Connection': 'keep-alive'
}

# 页数
pageindex = 1
# 滑动更新页
asyncreq = 1
# 参数data编码
sdata = urllib.parse.quote('关键词')  # quote()将字符串进行编码

conn.request("GET", "/data/ajax/get_premium_offer_list.json?"
                            "beginpage={}"
                            "&asyncreq={}"
                            "&keywords={}"
                            "&ptid=hr6cfd8516d30252"
                            "&hpageId="
                            "&provinceValue="
                            "&p_rs=true"
                            "&exp="
                            "&spm="
                            "&pageid="
                            "&p4pid="
                            "&salt="
                            "&sign="
                            "&callback="
                            "&_=1696829023464".format(pageindex, asyncreq, sdata), payload, headers)
res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")
return data
