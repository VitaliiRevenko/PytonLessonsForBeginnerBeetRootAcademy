'''Короткие задачи
Создать лист с днями недели.
В одну строку (ну или как обычно) создать словарь вида
{"Понедельник" : 1, ...
Так же в одну строку или как получится создать обратный словарь
{ 1: "Понедельник",'''

#print(week)
def DictRevers(items):
    new_dict = {}
    for key, value in items:
        key, value = value, key
        new_dict.setdefault(key, value)
    return new_dict
a = {'Понедельник': 1, 'Вторник': 2, 'Среда': 3, 'Четверг': 4, 'Пятница': 5, 'Суббота': 6, 'Воскресенье': 7}
b = DictRevers(a.items())
print(f'Original dict\t{a}\n Revers dict\t{b}')

