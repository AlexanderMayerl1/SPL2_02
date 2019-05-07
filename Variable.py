# variable.py

a=10
b=20
c=30

print (a+b+c)
print ("Summe =", a+b+c)

print ("Multiplikation", a*b)

print ("Division", a/b)
print ("Division", int(c/a))

print ("Potzenz", a**b)

text = "HalloWelt"

print (text * 99)

print ("-" * 20)
print (text)
print ("-" * 20)

#name = input("Wer bist du? ")
name = "MuratsBoerek"
print ("Hallo", name * 90)

for i in ("Murat", "Hamit", "Stella"):
	print(i)
	
for i in (-4, 12, 19, 7, 0, -281, 192):
	print(i, end=" ")
	
for i in range (1, 100):
	print(i, end=" ")
	
while(True):
	i += 1
	print (i, end=". ")