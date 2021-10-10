import random

# Запрашивать у пользователя команду.
# В зависимости от введенной команды выполнять действие.
todos = {}

HELP = '''
* help - напечатать справку по программе.
* add - добавить задачу в список (название задачи запрашиваем у пользователя).
* show - напечатать все добавленные задачи.
* random - добавить случайную задачу на сегодня
'''
# Дата:[Задача1, Задача2,....]
RANDOM_TASK = ["Главное не заснуть",
               'Выгулять собаку',
               'Учить английский']


def add_todo(date, task):
    if date in todos:
        todos[date].append(task)
    else:
        todos[date] = []
        todos[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')

#command = input("Введите команду: ")
while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        add_todo(date, task)
    elif command == 'show':
        date = input('Введите дату: ')
        if date in todos:
            for task in todos[date]:
                print(f'[] {task}')
        else:
            print("Задач на эту дату нет")
    elif command == 'random':
        date = 'сегодня'
        add_todo(date, random.choice(RANDOM_TASK))
    else:
        print("Неизвестная команда!")
        break
