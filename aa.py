import subprocess






url = 'http://open-tct.douyucdn2.cn/dyliveflv3/5720533rEC7Us8xF_2000.flv?wsAuth=e8bf7335105e480eb040a72780674436&token=cpn-androidmpro-0-5720533-0a608c69d2cbd2d2a6b2c70fafed469772a6a745a363f631&logo=0&expire=0&did=698c90e4c311fe1e99208886c7a13976&origin=tct&vhost=play3&sid=351694230'



ffm = subprocess.run(f"""bash -c 'ffmpeg -t 30 -i "{url}" -c:a copy -c:v copy -f segment -segment_time 60 -strftime 1 %Y-%m-%d-%H-%M-%S.mp4'""",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)







