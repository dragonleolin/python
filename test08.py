import requests
import pyquery
import codecs

# FACEBOOK = 'sb=AuiFXtXevVmYqYi3X57HO25p; datr=AuiFXs2K5zqqg2cdRxnALtqi; dpr=1.25; c_user=1533718531; xs=13%3AV2DGGup6kGxRlQ%3A2%3A1585834147%3A18481%3A11316; spin=r.1001998448_b.trunk_t.1587039033_s.1_v.2_; fr=1dqGx5vcLXt0H9YRf.AWVBhyd3c9NctTRlKyf8ZV3uOYY.BehegC.ux.F6X.0.0.BemE5q.AWVHNmLa; act=1587039851895%2F0; presence=EDvF3EtimeF1587039852EuserFA21533718531A2EstateFDutF1587039852617CEchF_7bCC; wd=1152x722'


def main():
response = requests.get(
'https://www.facebook.com',
headers={
'Cookie': 'sb=AuiFXtXevVmYqYi3X57HO25p; datr=AuiFXs2K5zqqg2cdRxnALtqi; dpr=1.25; c_user=1533718531; xs=13%3AV2DGGup6kGxRlQ%3A2%3A1585834147%3A18481%3A11316; spin=r.1001998448_b.trunk_t.1587039033_s.1_v.2_; fr=1dqGx5vcLXt0H9YRf.AWVBhyd3c9NctTRlKyf8ZV3uOYY.BehegC.ux.F6X.0.0.BemE5q.AWVHNmLa; act=1587039851895%2F0; presence=EDvF3EtimeF1587039852EuserFA21533718531A2EstateFDutF1587039852617CEchF_7bCC; wd=1152x722'
}
)
if response.status_code != 200:
print('facebook page download: failed')
return

d= pyquery.PyQuery(response.text)

elems = d('div.hidden_elem > code')
print(len(elems))

for elem in elems
    elem_html = elem.html()[5:-4]
    elem_d = pyquery.PyQuery(elem_html)
    if  elem_d('div.userContentWrapper') is None:
        continue
    print('article found')

if __name__ == '__main__':
main()