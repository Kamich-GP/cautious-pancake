import telebot
from telebot.types import ReplyKeyboardRemove
from buttons import kb

# Создать объект бота
bot = telebot.TeleBot('6769812309:AAHQDL4OkscI00iAYluWwKX_Blu0E-duC-Y')


# Обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Приветствую! Добро пожаловать в мой первый бот)',
                     reply_markup=kb)


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id

    if message.text.lower() == 'википедия':
        bot.send_message(user_id, 'Введите слово', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'переводчик':
        bot.send_message(user_id, 'Введите слово для перевода', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, tran)
    else:
        bot.send_message(user_id, 'Неизвестная операция')

def wiki(message):
    user_id = message.from_user.id

    if message.text.lower() == 'райан гослинг':
        bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D0%BB%D0%B8%D0%BD%D0%B3,_%D0%A0%D0%B0%D0%B9%D0%B0%D0%BD')
        bot.send_message(user_id, 'Готово, что еще?', reply_markup=kb)
        bot.register_next_step_handler(message, text_message)
    else:
        bot.send_message(user_id, 'Неизвестная операция')
        bot.register_next_step_handler(message, wiki)


def tran(message):
    user_id = message.from_user.id

    if message.text.lower() == 'hello':
        bot.send_message(user_id,
                         'Привет')
        bot.send_message(user_id, 'Готово, что еще?', reply_markup=kb)
        bot.register_next_step_handler(message, text_message)
    else:
        bot.send_message(user_id, 'Неизвестная операция')
        bot.register_next_step_handler(message, tran)

        
# Запуск бота
bot.polling(non_stop=True)
