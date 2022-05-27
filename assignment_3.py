# Write a Python program that returns a dictionary 
# which consists the unique elements in the following tuple as keys and 
# the number of occurrences of elements as values.


tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)

new = {}
s = set(tuple1) 

for i in s:
    new[i]=tuple1.count(i)

print(new)


