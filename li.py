import random
l=["s","p","si"]
print(l)
#print(l[1])
#print(l[0])
#print(l[4])
#print(l[5])
#for i in range(0,6):
	#print(i)
#l[1]=10
#print(l)
#print(l[1])
#print(len(l))
'''if "hi" in l:
	print("Yes")
else:
	print("No")'''
'''y = input("Enter your choice: ")
print("Hii ",y)'''
c = random.choice(l)

u = input("Enter your choice: ")
if u == c:
	print("It's a tie")
if c == 's' and u == 'si':
	print("C is the winner")
if c == 's' and u == 'p':
	print("U is the winner")
if c == 'si' and u == 'p':
	print("C is the winner")
if c == 'si' and u == 's':
	print("U is the winner")
if c == 'p' and u == 'si':
	print("U is the winner")
if c == 'p' and u == 's':
	print("C is the winner")
print(c)