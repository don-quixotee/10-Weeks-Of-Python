

def kay_sort(num):
	print("Orignal List : {}".format(num))
	for i in range(len(num)):
		for n in range(len(num) - 1):
			a = num[n]
			if (a > num[i]):
				tem = num[i]
				num[i] = a 
				num [n] = tem 
	return "Sorted List : {}".format(num)			
	
print(kay_sort([123, 4, 123, 4]))	
