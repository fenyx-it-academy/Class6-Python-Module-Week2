# HOMEWORK_1
# Write a Python program which executes following rules on this given list => numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# -take an input(number) from the user
# -take out the first element of the list and put it at the end. Do this x times that in the first step the user indicated.
# -print the list
# -(OPTIONAL) make sure there is not an error while taking input

numbers = []
for i in range(2,20):
    check = True
    for j in range(2,i):
        if(i%j == 0):
            check = False
            break
    if(check):
        numbers.append(i)

print(numbers)


n = int(input("Enter n: "))

for i in range(n):
    numbers.append(numbers.pop(0))

print(numbers)