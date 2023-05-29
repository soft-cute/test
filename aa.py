import requests
import json

def get_douyu_live_source(room_id):
    api_url = f"http://open.douyucdn.cn/api/RoomApi/room/{room_id}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if data["error"] == 0:
            live_source = data["data"]["rtmp_url"] + "/" + data["data"]["rtmp_live"]
            return live_source
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
    except (KeyError, ValueError, AttributeError) as e:
        print(f"解析错误: {e}")
    
    return None

# 使用示例
room_id = "101367"  # 替换成实际的房间ID
live_source = get_douyu_live_source(room_id)
if live_source:
    print(f"直播源：{live_source}")
else:
    print("获取直播源失败")
