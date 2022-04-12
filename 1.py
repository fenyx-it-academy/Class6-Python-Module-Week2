numbers=[2,3,5,7,11,13,17,19]
girdi=int(input('Bir sayi giriniz'))

i=1
while i<=girdi:
    a=numbers.pop(0)
    numbers.append(a)
    i+=1
print(numbers) 
