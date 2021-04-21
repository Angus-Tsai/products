import os
products = []
#讀取檔案
if os.path.isfile('products.csv'):#檢查檔案在不在
	print('成功找到檔案')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			s = line.strip().split(',')
			products.append(s)
	print(products)			
else:
	print('讀不到檔案')
#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])

#印出所有購買紀錄	
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案	
with open('products.csv', 'w', encoding='utf-8') as book:
	book.write('商品,價格\n')
	for p in products:
		book.write(p[0] + ',' + p[1] + '\n')