my_list = [7, 5, 3, 3, 2]
num = int(input("Enter a rating form 0 to 10: "))
for i in my_list:
    if num > i:
        m = my_list.index(i)
        my_list.insert(m, num)
        print(my_list)
        break
    if num <= my_list[-1]:
        my_list.append(num)
        print(my_list)
        break




# while True:
#     n = int(input("Enter a rating form 0 to 10: "))
#     if n < 0 or n > 10:
#         print("It isn't correct")
#     else:
#         k = my_list.count(n)
#         m = my_list.index(n)
#         my_list.insert(k + m, n)
#         print(my_list)
#
