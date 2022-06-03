# Write a Python program that returns a dictionary which consists the unique elements in the following tuple 
# as keys and the number of occurrences of elements as values.

tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)
occ_10 = occ_ = occ_20 = occ_50 = occ_60 = occ_70 = occ_80 = 0
Num_Occurences ={}
for item in tuple1:
    if item == 10:
        occ_10 = occ_10+1
Num_Occurences['10'] = occ_10
for item in tuple1:
    if item == 20:
        occ_20 = occ_20+1
Num_Occurences['20'] = occ_20
for item in tuple1:
    if item == 50:
        occ_50 = occ_50+1
Num_Occurences['50'] = occ_50
for item in tuple1:
    if item == 60:
        occ_60 = occ_60+1
Num_Occurences['60'] = occ_60
for item in tuple1:
    if item == 70:
        occ_70 = occ_70+1
Num_Occurences['70'] = occ_70
for item in tuple1:
    if item == 80:
        occ_80 = occ_80+1
Num_Occurences['80'] = occ_80
print(Num_Occurences)