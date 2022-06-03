# Write a Python program that returns the following dictionary with sorted values. 
# NOTE: Dictonaries have keys and values. Here the values are lists. So, the returned dictonary 
# should have sorted values(list) 
data = { 'a': [5, 3, 9, 0, 2, 3, 1], 'b': [4, 7, 5, 1, 2], 'c': [8, 1, 3, 2, 4] }
list_a = [5,3,9,0,2,3,1]
list_b = [4,7,5,1,2]
list_c = [8,1,3,2,4]
list_a.sort()
list_b.sort()
list_c.sort()
data['a'] = list_a
data['b'] = list_b
data['c'] = list_c
print(data)