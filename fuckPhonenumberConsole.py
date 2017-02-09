

import requests

duibi_url = 'http://car.autohome.com.cn/duibi/chexing/'
url = 'https://github.com/timeline.json'
'http://car.autohome.com.cn/duibi/ashx/SpecCompareHandler.ashx?type=2&seriesid=2970&isie6=0'
r = requests.get(duibi_url)
print r.text
print type(r.text)
# with open('temp.html', 'w') as temp_file:
#     temp_file.write(r.text)

