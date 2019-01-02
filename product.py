pr = []

while True:
	product = input('Enter the name of product. ')
	if product == 'end':
		break
	price = input ('Enter the price of product. ')
	p = []
	p.append(product)
	p.append(price)
	pr.append(p)
	

print(pr[0][1])
