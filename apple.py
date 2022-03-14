from rich.console import Console
console = Console()

x = 10

for y in range(3):
	if y ==2:
	    	console.print(' '*(int(x/2)-1),'#',style='green')

for y in range(5):
	if y == 0 or y == 4:
		console.print('#'*x+'\b','\r','')
	else:
		console.print('#'*x)
