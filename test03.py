c = [1, 2, 3, 4, 5, 6, 7, 8 , 9]



odds = [
    i
   for  i in c
    if i % 2 != 0 #test
]

print(odds)

stocks=[{
    'name': '2330',
    'age': 123
},{
    'name': '2303',
    'age': 40
}]

print([
    stock['name']
    for stock in stocks
    if stock ['close'] > 100
])