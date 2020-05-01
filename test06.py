import urllib.parse as up

url = 'https://24h.pchone.com.tw:8080/prod/DPAE1T-1900AHGHO?sort=asc&utm=123'

result = up.urlparse(url)

print(result.path)

print(result.path.split('/')[-1])

s='%E9%99%B3%E6%99%82%E4%B8%AD'

print(up.quote(s))

print(up.quote('陳時中'))