my_list = [62,2,999,23,9,39,24,56,784,7,4,6,3,5474]
new_list = (input('Input New List: ', []))


print('Unoedered list: ', my_list)

my_list.sort()
print('Ordered list: ', my_list, new_list)




#Morse code [01] to alphanumeric converter

a = 79

#Base 2(binary)

bin_a = bin(a)
print(bin_a)
print(int(bin_a, 2)) #Base 2 binary