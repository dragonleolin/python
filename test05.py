import json

s = '{"name": "john"}'

d=json.loads(s)

print(d['name'])

d=[{
    'name': 'marry'
}]
print(json.dumps(d))