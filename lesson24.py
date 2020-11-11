my_str = input("Введите элементы списка через пробел: ")
my_list = my_str.split()
for i,n in enumerate(my_list):
    print(i+1,n[:10])

