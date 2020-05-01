import requests
import urllib.parse as up

def search(word):
    word = up.quote(word)
    url = f'https://www.google.com/search?q={word}'

# response = requests.get(url)

# if response.status_code != 200:
#     print('request error')
#     return

# with open('google.html', 'wb') as f:
#  f.write(response.content)



if __name__ == '__main__':
    search('陳時中')