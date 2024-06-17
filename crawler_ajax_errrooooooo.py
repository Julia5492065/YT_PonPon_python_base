# 抓取 Medium.COM 的文章資料
import urllib.request as req
url="https://data.gov.tw/suggests?p=1&size=10&s=sid_desc"
#建立一個Request物件，附加Request Headers的資訊
request=req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")#根據觀察，取得的資料是 JSON 格式
# print(data)

#解析JSON格式的資料，取得每篇文章的標題
import json
# data=data.replace()
data= json.loads(data) #把原始的JSON資料解析成字典/列表的表示形式
#取得JSON資料中的文章標題
posts=data["payload"]["search_result"]
for key in posts:
    post=posts[key]
    print(post["title"])
