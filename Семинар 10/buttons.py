from telebot import types


def keyboard():
    kboard = types.InlineKeyboardMarkup()
    kboard.row(types.InlineKeyboardButton('7', callback_data='7'),
               types.InlineKeyboardButton('8', callback_data='8'),
               types.InlineKeyboardButton('9', callback_data='9'),
               types.InlineKeyboardButton('*', callback_data='*'))

    kboard.row(types.InlineKeyboardButton('4', callback_data='4'),
               types.InlineKeyboardButton('5', callback_data='5'),
               types.InlineKeyboardButton('6', callback_data='6'),
               types.InlineKeyboardButton('/', callback_data='/'))

    kboard.row(types.InlineKeyboardButton('1', callback_data='1'),
               types.InlineKeyboardButton('2', callback_data='2'),
               types.InlineKeyboardButton('3', callback_data='3'),
               types.InlineKeyboardButton('+', callback_data='+'))

    kboard.row(types.InlineKeyboardButton(',', callback_data=','),
               types.InlineKeyboardButton('0', callback_data='0'),
               types.InlineKeyboardButton('C', callback_data='C'),
               types.InlineKeyboardButton('-', callback_data='-'))

    kboard.row(types.InlineKeyboardButton('=', callback_data='='))

    return kboard


def start_buttons():
    markup = types.ReplyKeyboardMarkup(True, True)
    itembtn_1 = types.KeyboardButton('/Начать')
    itembtn_2 = types.KeyboardButton('/Помощь')
    markup.add(itembtn_1, itembtn_2)
    return markup
