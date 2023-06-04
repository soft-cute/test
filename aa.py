import datetime
import subprocess
import os
import sys
from aligo import Aligo


file = 'download/抖音录播/豆子❤️梨形身材女装/2023-06-03'
os.makedirs(file)
mp = os.path.join(file,'%Y-%m-%d-%H-%M-%S.mp4').replace('\\','/')
url = 'http://open-tct.douyucdn2.cn/dyliveflv1/1457640rTDKVcLaU_2000p.flv?wsAuth=9d10f3e3adfb859e01e83049dd3a3070&token=cpn-androidmpro-0-1457640-2f3e9731c8986be5ceab091b9684a6653123b11445a4d791&logo=0&expire=0&did=f282c65055f7f4a140307d16841e5291&origin=tct&vhost=play1&sid=351506882'
data = f"""bash -c 'ffmpeg -t 19800 -i "{url}" -c:a copy -c:v copy -preset superfast -f segment -segment_time 3600 -strftime 1 {mp}'"""

subout = subprocess.run(data,shell=True)

print(subout)
 
# Aligo()
# subprocess.run( """bash -c 'git add ./aaa.txt && git commit -m "Add changes" && git push --all'""",shell=True)