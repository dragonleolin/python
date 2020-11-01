import requests
from io import StringIO
import pandas as pd


# 指定爬取月報的網址
url = 'https://mops.twse.com.tw/nas/t21//t21sc03_109_9.html'
# 抓取網頁
r = requests.get(url)



r.encoding = 'big5'
dfs = pd.read_html(StringIO(r.text))

df = dfs[0]
df = df[list(range(20))]
df.columns = df[df[0]  == '公司代號'].iloc[0]
df = df.loc[~pd.to_numeric(df['當月營收'], errors='coerce').isnull()]
df = df.loc[~(df['公司代號'] =='合計')]
df = df.set_index(['公司代號', '公司名稱'])
df = df.apply(pd.to_numeric)
df 