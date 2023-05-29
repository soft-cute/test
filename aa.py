# 导入requests和ub98484234库
import requests
import ub98484234
import datetime,random,string
# 输入房间号
rid = input("请输入房间号：")
# 获取当前日期，格式为2501YYYYMMDD
date = datetime.datetime.now()
v = "2501" + date.strftime("%Y%m%d")
# 获取当前时间戳，单位为秒
tt = int(date.timestamp())
# 获取设备ID，可以随机生成一个32位的字符串
did = "".join(random.choices(string.ascii_letters + string.digits, k=32))
# 获取版本号，固定为22011191
ver = 22011191
# 获取清晰度，-1为默认
rate = -1
# 调用ub98484234函数，传入参数，获取签名
sign = ub98484234.ub98484234(rid, did, tt)
# 发送POST请求，获取直播源网址
data = {
    "v": v,
    "did": did,
    "tt": tt,
    "sign": sign,
    "ver": ver,
    "rid": rid,
    "rate": rate
}
resp = requests.post("https://m.douyu.com/api/room/ratestream", data=data).json()
# 拼接rtmp_url和rtmp_live两个值
url = resp["data"]["rtmp_url"] + "/" + resp["data"]["rtmp_live"]
# 输出直播源网址
print(url)