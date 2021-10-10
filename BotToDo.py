import telebot
import random
from random import choice

token = '2038991391:AAEvyEAIf39s0iz4aoeM_36qh_FKdpGZSbA'

bot = telebot.TeleBot(token)

todos = {}

HELP = '''
Список доступных команд:
*show - напечатать все задачи на заданную дату
* help - напечатать список доступных команд
* add - добавить задачу в список (название задачи запрашиваем у пользователя).
* random - добавить случайную задачу на сегодня
'''

RANDOM_TASKS = ["Главное не заснуть",
               'Выгулять собаку',
               'Учить английский']

def add_todo(date, task):
    if date in todos:
        todos[date].append(task)
    else:
        todos[date] = []
        todos[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')

#Декораторы
#@bot.message_handler(content_types=["text"])(echo)
@bot.message_handler(commands=["help"])
def echo(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["random"])
def random_task(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=["show", "print"])
def show(message):
    date = message.text.split()[1]
    date = date.lower()
    if date in todos:
        reply = date.upper() + '\n'
        for task in todos[date]:
            reply += f'{task}\n'
    else:
        reply = "Такой даты нет"
    bot.send_message(message.chat.id, reply)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    splitted_command = message.text.split(maxsplit=2)
    date = splitted_command[1]
    task = splitted_command[2]
    add_todo(date, task)
    bot.send_message(message.chat.id, f"Задача {task} на дату {date}")



bot.polling(none_stop=True)