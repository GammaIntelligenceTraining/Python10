'''
Программа заметок:
дата добавления
заголовок
содержание
дата выполнения
уникальный ID

database - json file

создать заметку
выбрать заметку
вывести список заметок
загрузить/сохранить базу
'''
import json
import datetime

base = {}

def create_note():
    title = input('Enter note title: ')
    content = input('Enter note content: ')
    while True:
        due_date = input('Enter date (YYYY-MM-DD): ')  # YYYY-MM-DD
        if due_date.lower() == 'exit':
            return None
        try:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        except:
            print('Error, try again or type "exit"!')
        else:
            break
    return {'title': title, 'content': content, 'due_date': str(due_date), 'created': str(datetime.date.today())}

def save_new_note(note):
    load_base()
    base['notes'][note['title']] = note
    print(base)
    with open('db.json', 'w') as file:
        json.dump(base, file, indent=2)

def load_base():
    global base
    with open('db.json', 'r') as file:
        base = json.load(file)

save_new_note(create_note())
# create_note()