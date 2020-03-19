'''Пишем игру в 21. Создать массив
"карт" рандомно их перемешать и выдавать
"игроку" пока не скажет стоп или не проиграет.

import random
coloda = [2, 3, 4, 6, 7, 8, 9, 10, 11 ] *4
print(coloda)'''
#list_alphabet = list("абвгде")
'''countries = ['Ukraine', 'Poland', 'France', 'Germany', 'Finland','Ukraine', 'Poland', 'France', 'Germany', 'Finland']
for i, country in enumerate(countries):
    countries[i] = (country, i+1)
print(countries)'''
'''sevens = []
for i in range(71):
    if i % 7 ==0:
        sevens.append(i)
print(sevens)

sevens = []
i = 0
while i<= 70:
    sevens.append(i)
    i += 7
print(sevens)
##################
import random
points = 0
while True:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print('points: ' + str(points))
    answer = input (str(x) + '+' + str(y) + '=? (type q to quit): ')
    if answer == 'q':
        break
    elif int(answer) != x+y:
        print('No points for you')
        continue
    print('Good job')
    points += 1'''
######################
country = {'name' : 'Sweden', 'capital': 'Stockholm',
           'largest_cities': ['Stokholm', 'Gothenburg', 'Malmo']}
#country['population'] = 1000000
#country.update({'population': 1000000, 'languange': 'Swedish'})
#for key, value in country.items():
#    print((key, ':', value))
#print(country)
#empty_dict = {}
#empty_set = set()
#print(type(empty_dict))
#print(type(empty_set))
######################
#task1
'''stroka = str(input('Vvedite predlozhenie:\t'))
print(list(stroka.split(' ')))
print(stroka[1])'''
########################
str = input("Write down or insert some text:\n")
punctuation = ['.',',',':',';','!','?','(',')']
wordList = str.split()
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1
    
print(set(wordList))
print(wordList[1])

'''i = 0
while i < len(wordList):
    print(wordList[i], end=' ')
    i += 1
    if i%5 == 0:
        print()'''