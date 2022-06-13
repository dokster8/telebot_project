import telebot
from telebot import types
from settings import token
from bashe_game_copy import start_turn
from calc import calc_result

bot = telebot.TeleBot(token)
print('Server on-line')


@bot.message_handler(commands=['help', 'start'])
def help_command(message):
    bot.send_message(message.from_user.id,
                     'Доступные команды:\n/help\n/calc "математическое выражение"')


@bot.message_handler(commands=['calc'])
def calc_comand(message):
    args = message.text.split()
    operation = ''.join(args[1:])
    result = calc_result(operation)
    bot.send_message(message.from_user.id, f'{operation} = {result[0]}')


# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('1⃣ Начать 1⃣')
#     bot.send_message(message.from_user.id,
#                      f'Привет {message.from_user.first_name}!\nНачнём игру?', reply_markup=user_markup)


# @bot.message_handler(regexp='1⃣ Начать 1⃣')
# def start_game(message):
#     bot.send_message(message.from_user.id,
#                      'Отлично, начнём!\nПравила игры:\nВ куче лежит 234 конфет. Каждый ход Вы и я будем брать конфеты. За один ход необходимо брать не более 27 конфет. Взявший последние конфеты побежадет!')
#     # bot.send_message(message.from_user.id, 'Ты ходишь. Сколько берешь конфет?')
#     start_turn(message)


# @bot.message_handler(commands=['hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет, сыграем?")


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, 'Привет, сыграем?')
bot.infinity_polling()

print('Server off-line')
