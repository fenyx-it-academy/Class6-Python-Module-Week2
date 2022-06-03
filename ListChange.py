# Write a Python program which executes following rules on this given list =>
#  numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# -take an input(number) from the user
# -take out the first element of the list and put it at the end. Do this x times that in the first step the user indicated.
# -print the list
# -(OPTIONAL) make sure there is not an error while taking input

numbers = [2,3,5,7,11,13,17,19]

while True:
    i = 0
    try:
        number_exe = int(input('Please Enter The Number of Execution : '))
    except ValueError:
        print("Please Input Integer Only - TRY Again...")
        continue
    while i<number_exe:
        first = numbers[0]
        numbers.pop(0)
        numbers.append(first)
        print(numbers)
        i +=1    