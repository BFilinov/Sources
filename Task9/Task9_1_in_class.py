import re
import datetime

path = './nasa_19950801.tsv'
data_pattern = r'\s(\d{9})\s'
url_pattern_start = '^[^\s]+'
url_pattern_finish = r'\/[^\s]+'

try:
    fc = open(path)
    txt = fc.read()
    m1 = list(map(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'),
                  re.findall(data_pattern, txt)))
    m2 = re.findall(url_pattern_start, txt, flags=re.MULTILINE)
    m3 = re.findall(url_pattern_finish, txt)
    full_list = list(zip(m1, m2, m3))
    dc = {}
    for k in full_list:
        gets = dc.get(k[0])
        tp = (k[1] + k[2],)
        if gets is None:
            dc[k[0]] = tp
        else:
            dc[k[0]] += tp

    for k, v in dc.items():
        print('{}: {}'.format(k, v))
finally:
    fc.close()
