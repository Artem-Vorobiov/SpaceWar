import random

colors = ['darkorange', 'black', 'red', 'white', 'purple']

# for i in range(5):
# 	digit = random.randint(0,4)
# 	print(colors[digit])


# for i in range(10):
# 	print(type(random.randint(-280,280)))

# if type(colors) == list:
# 	print('YEAH')
# else:
# 	print('nope')

somelist = [1,2,3,4,5,6,7,8,9,10]
count = 0
print(somelist)

for x in somelist[:]:
	print('\t {}'.format(x))
	somelist.remove(x)
	# del somelist[count-1]
	# count += 1

# for i in range(len(somelist)+1):
# 	print(i)
# 	del somelist[i-1]

print(somelist)