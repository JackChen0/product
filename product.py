pr = []

while True:
	product = input('Enter the name of product. ')
	if product == 'end':
		break
	price = input ('Enter the price of product. ')
	pr.append([product,price])
	

print(pr)
for p in pr:
	print('The price of ',p[0],'is', p[1])