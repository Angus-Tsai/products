import os
#讀取檔案
def read_file(filename, products):
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			s = line.strip().split(',')
			products.append(s)
	print(products)
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	return products
		
#印出所有購買紀錄	
def trading_record(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as book:
		book.write('商品,價格\n')
		for p in products:
			book.write(p[0] + ',' + p[1] + '\n')



def main(filename):
	products = []
	if os.path.isfile(filename):#檢查檔案在不在
		print('成功找到檔案')
		read_file(filename, products)
	else:
		print('讀不到檔案')
	user_input(products)
	trading_record(products)
	write_file(filename, products)

main('products.csv')