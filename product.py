pr = []
#讀取檔案
with open('product.csv', 'r', encoding = 'utf-8') as r: 
	for line in r:
		if 'product, price' in line:
			continue
		product, price = line.strip().split(',')
		pr.append([product, price])

while True:
	product = input('Enter the name of product. ')
	if product == 'end':
		break
	price = input ('Enter the price of product. ')
	price = int(price)
	pr.append([product,price])
#輸入資料
print(pr)
for p in pr:
	print('The price of ',p[0],'is', str(p[1]))
#寫入檔案
with open('product1.csv', 'w', encoding = 'utf-8') as f:
	f.write('name, price\n')
	for p in pr:
		f.write(p[0] + ','+ str(p[1]) + '\n')