#primes.py
# alle primzahlen von 1 bis 1000

for i in range(1, 1001):
	for y in(2, i):
		if(i%y== 0):
			if(y == i):
				print(i)
			break
