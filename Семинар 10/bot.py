import config
import telebot
import buttons
import datetime

dtn = datetime.datetime.now()

bot = telebot.TeleBot(config.TOKEN)
value = ''
old_value = ''


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user
    user = message.from_user.first_name
    bot.send_message(message.chat.id,
                     f"Привет, {user}!\n"
                     "Это бот-калькулятор, чтобы начать им пользоваться нажми 'Начать'\n"
                     "Чтобы перейти в раздел помощи, нажми 'Помощь'",
                     reply_markup=buttons.start_buttons())


@bot.message_handler(commands=['help', 'Помощь'])
def send_help(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Это бот-калькулятор. Доступные команды\n'
                          '/calc или /Начать для старта работы калькулятора\n'
                          '/logs для скачивания логов\n'
                          '/help или /Помощь для перехода в раздел помощь\n'
                          '/start для просмотра приветствия')


@bot.message_handler(commands=['logs'])
def send_logs(message):
    bot.send_document(chat_id=message.chat.id, document=open('Logs.log', 'rb'))


@bot.message_handler(commands=['calc', 'Начать'])
def calculator(message):
    global value
    if value == '':
        bot.send_message(message.chat.id, text='Калькулятор! Давай считать!', reply_markup=buttons.keyboard())
    else:
        bot.send_message(message.chat.id, text=f'Калькулятор! Давай считать!\n{value}', reply_markup=buttons.keyboard())


@bot.callback_query_handler(func=lambda call: True)
def calculation(call):
    global value, old_value
    data = call.data
    if data == 'C':
        value = ''
    elif data == "=":
        try:
            inf = str(value)
            value = str(eval(value))
        except:
            value = 'Ошибка'
        botlogfile = open('Logs.log', 'a')
        print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь_id ' + str(call.message.chat.id),
              'произвел расчет ' + inf + " = " + value, file=botlogfile)
        botlogfile.close()
    else:
        value += data
    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Калькулятор! Давай считать!\n0',
                                  reply_markup=buttons.keyboard())
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'Калькулятор! Давай считать!\n{value}',
                                  reply_markup=buttons.keyboard())
            old_value = value

    if value == 'Ошибка': value = ''


bot.infinity_polling(skip_pending=True)
