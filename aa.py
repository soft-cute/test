import datetime
import subprocess
import os
import sys
from aligo import Aligo



os.makedirs('download/抖音录播/豆子❤️梨形身材女装/2023-06-03/')
aaa = subprocess.run('bash -c "ffmpeg -t 19800 -i "http://pull-flv-l26.douyincdn.com/stage/stream-689590783250268299_or4.flv?expire=6484347c&sign=cfc2b1fde60f391b4b808d88a87bfe99" -c:a copy -c:v copy -f segment -segment_time 3600 -strftime 1 download/抖音录播/豆子❤️梨形身材女装/2023-06-03/%Y-%m-%d-%H-%M-%S.mp4"',shell=True)

print(aaa)
 
Aligo()