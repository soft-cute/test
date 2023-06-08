import subprocess






url = 'http://open-tct.douyucdn2.cn/dyliveflv3/5720533rEC7Us8xF_2000.flv?wsAuth=eda9775210b9112de1f4c40f3a8c80dc&token=cpn-androidmpro-0-5720533-0a608c69d2cbd2d2108d8219d023e1a0bad1fbc09ab0ceaf&logo=0&expire=0&did=4cf83f7b4258944ba621231457fb1ac4&origin=tct&vhost=play3&sid=351694230'



ffm = subprocess.run(f"""bash -c 'ffmpeg -t 30 -i "{url}" -c:a copy -c:v copy -f segment -segment_time 60 -strftime 1 %Y-%m-%d-%H-%M-%S.mp4'""",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)







