'''Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j)
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.'''

i, j = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []
index = 0
while index <= 9:
    j.append(i[index] * i[index])
    index += 1
print(f'{i}\n{j}')

