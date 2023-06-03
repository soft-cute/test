import datetime
import subprocess
import os
import sys
from aligo import Aligo


# file = 'download/抖音录播/豆子❤️梨形身材女装/2023-06-03'
# os.makedirs(file)
# mp = os.path.join(file,'%Y-%m-%d-%H-%M-%S.mp4').replace('\\','/')
# url = 'http://open-tct.douyucdn2.cn/dyliveflv3a/115280rZMKulyF7Q_2000.flv?wsAuth=9155c8b109f4c32236cbfcaaf2f49406&token=cpn-androidmpro-0-115280-580dca762c3607264118cbc28271899d1c514268ca9df17e&logo=0&expire=0&did=a6b66c7c81a583ee867932bbc99f238a&origin=tct&vhost=play4&sid=351418660'
# data = f"""bash -c 'ffmpeg -t 19800 -i "{url}" -c:a copy -c:v copy -f segment -segment_time 3600 -strftime 1 {mp}'"""

# subout = subprocess.run(data,shell=True)

# print(subout)
 
# Aligo()
subprocess.run( 'bash -c "git add ./aaa.txt && git commit -m "Add changes" && git push --all"',shell=True)