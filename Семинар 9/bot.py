import telebot
from telebot import types
from fractions import Fraction

# TOKEN = '5917360295:AAEsHd4ydcG5RYDyxbi8G30l0EeLWEBeCBU'
bot = telebot.TeleBot("5917360295:AAEsHd4ydcG5RYDyxbi8G30l0EeLWEBeCBU")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Калькулятор для комплексных или рациональных чисел\nДля того чтобы начать введите /start")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    itembtn_1 = types.KeyboardButton('Комплексные')
    itembtn_2 = types.KeyboardButton('Рациональные')
    markup.add(itembtn_1, itembtn_2)
    bot.send_message(message.chat.id, "С какими числами будем работать?", reply_markup=markup)


markup_2 = types.InlineKeyboardMarkup(row_width=4)
markup_2.add(types.InlineKeyboardButton('*', callback_data='*'))
markup_2.add(types.InlineKeyboardButton('/', callback_data='/'))
markup_2.add(types.InlineKeyboardButton('+', callback_data='+'))
markup_2.add(types.InlineKeyboardButton('-', callback_data='-'))


@bot.message_handler(func=lambda m: True)
def comp_or_frac(message):
    if message.text == 'Комплексные':
        num_one = bot.send_message(message.chat.id,
                                   "Введите первое комплексное число в формате x+yj\nили коэффициенты через запятую")
        bot.register_next_step_handler(num_one, num_1_complex)
    elif message.text == 'Рациональные':
        num_one = bot.send_message(message.chat.id,
                                   "Введите первое рациональное\n число в формате дроби x/y \nили через запятую")
        bot.register_next_step_handler(num_one, num_1_fraction)


def num_1_complex(message):
    global num_1
    num_1 = message.text
    if "j" in num_1:
        num_1 = complex(num_1)
    else:
        num_1 = num_1.split(",")
        num_1 = complex(int(num_1[0]), int(num_1[1]))
    num_two = bot.send_message(message.chat.id, "Введите второе комплексное число")
    bot.register_next_step_handler(num_two, num_2_complex)


def num_2_complex(message):
    global num_2
    num_2 = message.text
    if "j" in num_2:
        num_2 = complex(num_2)
    else:
        num_2 = num_2.split(",")
        num_2 = complex(int(num_2[0]), int(num_2[1]))
    msg = bot.send_message(chat_id=message.chat.id, text="Выбери действие", reply_markup=markup_2)
    bot.register_next_step_handler(msg, operation)


def num_1_fraction(message):
    global num_1
    num_1 = message.text
    if "/" in num_1:
        num_1 = num_1.split("/")
        num_1 = Fraction(int(num_1[0]), int(num_1[1]))
    else:
        num_1 = Fraction(num_1)

    num_two = bot.send_message(message.chat.id, "Введите второе рациональное число")
    bot.register_next_step_handler(num_two, num_2_fraction)


def num_2_fraction(message):
    global num_2
    num_2 = message.text
    if "/" in num_2:
        num_2 = num_2.split("/")
        num_2 = Fraction(int(num_2[0]), int(num_2[1]))
    else:
        num_2 = Fraction(num_2)
    msg = bot.send_message(chat_id=message.chat.id, text="Выбери действие", reply_markup=markup_2)
    bot.register_next_step_handler(msg, operation)


@bot.callback_query_handler(func=lambda call: True)
def operation(call):
    global operation
    operation = call.message
    if call.data == '+':
        result = num_1 + num_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{num_1}{call.data}{num_2} = {result}")
    elif call.data == '-':
        result = num_1 - num_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{num_1}{call.data}{num_2} = {result}")
    elif call.data == '*':
        result = num_1 * num_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{num_1}{call.data}{num_2} = {result}")
    elif call.data == '/':
        result = num_1 / num_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{num_1}{call.data}{num_2} = {result}")


bot.infinity_polling(skip_pending=True)
