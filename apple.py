from colorama import Fore,Style

x = 10

for y in range(3):
	if y ==2:
	    	print(Fore.GREEN + ' '*(int(x/2)-1),'#')

for y in range(5):
	if y == 0 or y == 4:
		print(Fore.RED + '#'*x+'\b','\r','')
	else:
		print(Fore.RED + '#'*x)

print(Style.RESET_ALL)
