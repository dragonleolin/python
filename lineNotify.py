import requests


response = requests.post(
    'https://notify-api.line.me/api/notify',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer cPWbQuPO6sIFHTXWHatXPE9I2nvLncMYCmLeNVDxwJT'
    },
    data={
        'message': 'Hello'
    }
)


print(response.status_code)
print(response.json())
