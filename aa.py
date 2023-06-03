import datetime
import subprocess
import os
import sys
from aligo import Aligo


file = 'download/抖音录播/豆子❤️梨形身材女装/2023-06-03'
os.makedirs(file)
mp = os.path.join(file,'%Y-%m-%d-%H-%M-%S.mp4').replace('\\','/')
url = 'http://open-tct.douyucdn2.cn/dyliveflv1a/1457640rTDKVcLaU_2000p.flv?wsAuth=60214c3bb779c4984bca1f5b024e7f67&token=cpn-androidmpro-0-1457640-2f3e9731c8986be5d6f67097f504a9cd4f8bf1fdeef00c8a&logo=0&expire=0&did=a6b66c7c81a583ee867932bbc99f238a&origin=tct&vhost=play2&sid=351402024'
# aaa = subprocess.run('bash -c \"ffmpeg -t 19800 -i \"http://pull-hs-f5-hot.flive.douyincdn.com/thirdgame/stream-113130789817287434_expuhd.flv" -c:a copy -c:v copy -f segment -segment_time 3600 -strftime 1 download/抖音录播/豆子❤️梨形身材女装/2023-06-03/%Y-%m-%d-%H-%M-%S.mp4\"',shell=True)
# data = 'bash -c "ffmpeg -t 19800 -i \\\"http://open-tct.douyucdn2.cn/dyliveflv1a/1457640rTDKVcLaU_2000p.flv?wsAuth=60214c3bb779c4984bca1f5b024e7f67&token=cpn-androidmpro-0-1457640-2f3e9731c8986be5d6f67097f504a9cd4f8bf1fdeef00c8a&logo=0&expire=0&did=a6b66c7c81a583ee867932bbc99f238a&origin=tct&vhost=play2&sid=351402024\\\" -c:a copy -c:v copy -f segment -segment_time 3600 -strftime 1 download/抖音录播/豆子❤️梨形身材女装/2023-06-03/%Y-%m-%d-%H-%M-%S.mp4"'
data = f"""bash -c 'ffmpeg -t 19800 -i "{url}" -c:a copy -c:v copy -f segment -segment_time 3600 -strftime 1 {mp}'"""

# aaa = subprocess.run(data,shell=True)
aaa = os.system(data)

print(aaa)
 
Aligo()