name = 'Vitalii'
surname = 'Revenko'
day = '7 march'

# task1
print("Good day",name,"!", day, "is a perfect day to learn some python")

#task2

print('Hello', name + ' ' + surname , '!')

#task3
a = 2
b = 3
print(a+b)
print(a-b)
print(a*b)
print (a/b)
print (a ** b)
print(a // b)
print(a % b)

#task *
s1 = "Корован"
''' print(s1[4], s1[3], s1[2], s1[1], s1[6], s1[5])
    print(f'{s1[1:-2]}')
    print(f'{s1[::-1]}')'''

s_inverse = s1[::-1]    #inverse 's1'
s2 = s_inverse[2:6]     #slise from 2 to 6 simbol
s3 = s_inverse[:2]      #slise 2 last simbols
s4 = s2 + s3            #write in 's4' sum 's2' and 's3'
print(s4.capitalize())  #first character converted to uppercase and all other characters converted to lowercase
