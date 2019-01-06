pr = []

while True:
	product = input('Enter the name of product. ')
	if product == 'end':
		break
	price = input ('Enter the price of product. ')
	price = int(price)
	pr.append([product,price])
	

print(pr)
for p in pr:
	print('The price of ',p[0],'is', str(p[1]))

with open('product.csv', 'w') as f:
	f.write('name, price\n')
	for p in pr:
		f.write(p[0] + ','+ str(p[1]) + '\n')