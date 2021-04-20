products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
for p in products:
	print(p[0], '的價格是', p[1])
with open('products.csv', 'w', encoding='utf-8') as book:
	book.write('商品,價格\n')
	for p in products:
		book.write(p[0] + ',' + p[1] + '\n')