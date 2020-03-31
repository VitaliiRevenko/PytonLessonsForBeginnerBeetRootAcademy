# Python program to update 
# JSON 


import json

# function to add to JSON 
def write_json(data, filename='data_file.json'):
    with open(filename, 'w') as f:
        print(json.dump(data, f, indent=4))
try:
    action = int(input('Введите "1" если хотите найти контакт\n' + \
                             'Введите "2" если хотите добавить новый контакт\n' + \
                             'Введите "3" если хотите удалить контакт\n' + \
                             'Введите "4" если хотите просмотреть всю адресную книгу\n' + \
                             'Ввести здесь ------->:'))
except ValueError:
    print('\n\nНе корректный ввод!!!\n')
    print('Необходимо ввести целое число!!!\n\n')

with open('data_file.json') as json_file:
    data = json.load(json_file)
    slovar = data.get("telephone_book")
    print(data)
    temp = []
    # python object to be appended
if action == 1:
    search = {}
    search['first_name'] = input('Для поиска контакта введите его имя:  ')
    search['last_name'] = input('Для поиска контакта введите его фамилию:  ')
    temp.append(search)
    for i in slovar:
        for key, value in i.items():
           if value == search['first_name']:
            print(key, ':', value)
    print(temp)
elif action == 2:
    add = {}
    add['first_name'] = input('Для добавления контакта введите его фамилию: ')
    add['last_name'] = input('Для добавления контакта введите его имя: ')
    add['telephone_number'] = input('Для добавления телефонного номера контакта введите его номер: ')
    # appending data to emp_details
    temp.append(add)
    print(add)
    print(temp)
    write_json(temp)
elif action == 3:
    delete = {}
    delete['first_name'] = input('Для удаления контакта введите его имя: ')
    delete['last_name'] = input('Для удаления контакта введите его фамилия: ')
    for i in slovar:
        for key, value in i.items():
            if value == delete['first_name'] and value == delete['last_name']:
                dict.popitem(key)
            #print(key, ':', value)
    print(slovar)
elif action == 4:
    for i in slovar:
        for key, value in i.items():
            print(key, ':', value)
        print('-'*25)
write_json(data) 
