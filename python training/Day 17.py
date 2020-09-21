##try:
##	if '5' < 6:
##		print("Hi")
##except TypeError:
## 	print("Hello")
##except ValueError:
##	print("Hey")
##else:
##	print("Holla")

##x = 5
##try:
##	if x % 2 == 0:
##		print("Hi" + x)
##except TypeError:
## 	print("Hello")
##except ValueError:
##	print("Hey")
##else:
##	print("Holla")

##x = []
##try:
##	if sum([1, 2] + (3, 4)) % 2 == 0:
##		x.append(1)
##		print(x)
##except TypeError:
##	x.append(2)
##	print(x)
##finally:
##	x.append(3)
##	print(x)

##pool = [2, (3), 9, '4', (5,), 1, [8]]
##total = 0
##others = []
##for item in pool:
##	try:
##		total += int(item)
##	except TypeError:
##		others.append(item)
##
##print(total, "and", others)

pool = [2, (3), 9, '4', (5,), 1, [8]]
total = 0
for item in pool:
	try:
		total += int(item)
	except TypeError:
		break

print(total)
