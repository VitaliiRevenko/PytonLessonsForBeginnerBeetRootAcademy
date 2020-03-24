'''Короткие задачи
Создать лист с днями недели.
В одну строку (ну или как обычно) создать словарь вида
{"Понедельник" : 1, ...
Так же в одну строку или как получится создать обратный словарь
{ 1: "Понедельник",
'''
'''
a = {'Понедельник': 1, 'Вторник': 2, 'Среда': 3, 'Четверг': 4, 'Пятница': 5, 'Суббота': 6, 'Воскресенье': 7}
b = dict([(i, j) for (j, i) in a.items()])
print(f'Original dict\t{a}\n Revers dict\t{b}')
'''

##################
'''1. программа играет с человеком угадывая загаданное число.
 но не методом урезания промежутка пополам, а выбирая рандомное число из промежутка.
import random
human = int(input('Vvedite celoe chislo \t'))
while True:
    r = random.randint(0, human)
    if r == human:
        print(f'Your number:\t{r}')
        break
    else:
        pass
'''
##################
'''2. пока человек не введет q или Q или Й или й играем с ним в камень ножницы бумага.
 сделайте множество или кортеж для набора вариантов. Рандомно выбирайте один из элементов листа (random.choice).
2.1 для игры допишите учет статистики в словарь
stats = {
"K": 0, "N": 0, "B":0 }
stats["K"] увеличиваем если человек загадал камень и так далее.
подумайте и допишите если есть больше 10 игр учет статистики предпочтений в качестве веса для рандома.
 (не случайно выбирать ПОТОМ фигуру а с учетом статистики. Делать рандом с учетом веса это пока рано но можете попробовать.
  Пока циклы условия, списки, вхождение в кортеж, редактирование словарика статистики )'''
import random
stone, scissors, paper = 1, 2, 3

win = (paper, stone), (stone, scissors), (scissors, paper)
lose = (stone, paper), (scissors, stone), (paper, scissors)
draw = (stone, stone), (scissors, scissors), (paper, paper)
while True:
    stats = {'stone': 0, 'scissors': 0, 'paper': 0}
    player = int(input(f'1 - Stone\n2 - Scissors\n3 - Paper\nEner the number:\t'))
    comp = random.randint(1, 3)
    if player == 1:
        stats['stone'] += 1
    elif player == 2:
        stats['scissors'] += 1
    elif player == 3:
        stats['paper'] += 1
    stats.update()
    comb = (player, comp)
    print(f'player:\t{player}\tcomp:\t{comp}')
    for i in win:
        if comb == i:
            print('You WIN')
    for j in lose:
        if comb == j:
            print('You LOSE')
        else:
            continue
    for x in draw:
        if comb == x:
            print('DRAW')
        else:
            continue
    finish = input("For exit push 'q'\t")
    if finish in {'q', 'Q'}:
        print(comb)
        break
    elif finish in {'й', 'Й'}:
        print(stats)
        break
