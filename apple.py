x = 10

for y in range(3):
	if y ==2:
		print(' '*(int(x/2)-1),'#')

for y in range(5):
	if y == 0 or y == 4:
		print('#'*x+'\b','\r','')
	else:
		print('#'*x)
