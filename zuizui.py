# coding:utf-8

import urllib.request
import re


#斗破苍穹 第2季
#url = r'http://v.qq.com/detail/8/8j37ljw0f8hy6ha.html'

#斗破苍穹
#url = r'https://v.qq.com/detail/l/lcpwn26degwm7t3.html'

#峡谷重案组 第2季
#url = r'https://v.qq.com/detail/k/k56xc7feh9s5o3d.html'

#斗罗大陆2 绝世唐门
#url = r'https://v.qq.com/detail/a/atk62w0bq58dnq9.html'

#雄兵连（下） 乾坤篇
#url = r'https://v.qq.com/detail/0/0zmk4a7exg3q6fa.html'

#斗罗大陆 第1季
#url = r'https://v.qq.com/detail/m/m441e3rjq9kwpsc.html'

html_text = str(urllib.request.urlopen(url).read(), 'utf-8')
html = re.findall(r'<span class="type_tit">更新时间:</span>.+?<span class="type_txt">(.+?)</span>', html_text, re.S)
print(html)
