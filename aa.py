# 导入需要的模块
import requests
import re
import time
import execjs

# 定义一些参数和变量
room_id = "101" # 直播间ID，根据实际情况修改
did = "5533423942ce86e564901f2200001631" # 设备ID，可以随机生成或固定使用
ver = "22011191" # 版本号，可以从斗鱼网页源码中找到
rate = "-1" # 清晰度，-1表示默认

# 获取斗鱼网页源码
url = f"https://m.douyu.com/{room_id}"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.88"
}
response = requests.get(url, headers=headers)
html = response.text

# 从网页源码中提取函数和变量
pattern1 = r"function ub98484234\([\w\W]*?}\)"
pattern2 = r"\w+=\[[\w\W]*?\];"
function = re.search(pattern1, html).group()
variable = re.search(pattern2, html).group()

aaa = """
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;\n
"""
# 拼接函数和变量为完整的js代码
js_code = aaa + variable + function

# 执行js代码，获取sign参数
context = execjs.compile(js_code)
v = "2501" + time.strftime("%Y%m%d") # v参数由2501和当前日期拼接而成
tt = str(int(time.time())) # tt参数为当前时间戳
sign = context.call("ub98484234", room_id, did, tt) # sign参数由执行js函数得到

# 构造post请求，获取直播流地址
post_url = "https://m.douyu.com/api/room/ratestream"
post_data = {
    "v": v,
    "did": did,
    "tt": tt,
    "sign": sign,
    "ver": ver,
    "rid": room_id,
    "rate": rate
}
post_headers = {
    "User-Agent": headers["User-Agent"],
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": url
}
post_response = requests.post(post_url, data=post_data, headers=post_headers)
post_json = post_response.json()

# 从json数据中提取rtmp_url和rtmp_live，拼接为完整的直播流地址
rtmp_url = post_json["data"]["rtmp_url"]
rtmp_live = post_json["data"]["rtmp_live"]
stream_url = rtmp_url + "/" + rtmp_live

# 打印直播流地址
print(stream_url)
