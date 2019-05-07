#primes.py
# alle primzahlen von 1 bis 1000

for i in range(1, 1001):
	for y in(2, 3, 5, 7):
		if(i%y != 0):
			break
		elif(y == 7):
			print(i)
