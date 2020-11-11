my_list = ['Winter', "Spring", "Summer", "Autumn", 'Winter']

while True:
    month = int(input('Enter a number of month: '))
    if month < 0 or month > 12:
        print("Enter correct number of month from 1 to 12!")
    else:
        print(my_list[month // 3])
        break

