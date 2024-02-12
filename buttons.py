from telebot import types

# Создаем пространство для кнопок
kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создаем сами кнопки
wiki = types.KeyboardButton('Википедия')
translate = types.KeyboardButton('Переводчик')

# Добавляем кнопки в пространство
kb.add(wiki, translate)

