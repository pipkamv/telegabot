from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# url_btn = InlineKeyboardButton(text='go to url', url='https://www.google.com')

m = KeyboardButton('Меню')
card = KeyboardButton('Корзина')
menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(m, card)

add_to_cart1 = InlineKeyboardButton(text='Добавить в корзину: ', callback_data='add1')
descriptonal = InlineKeyboardMarkup(text='Подробнее', callback_data='desc1')
btns1 = InlineKeyboardMarkup(row_width=2).row(add_to_cart1, descriptonal)


add_to_cart2 = InlineKeyboardButton(text='Добавить в корзину: ', callback_data='add2')
descriptona2 = InlineKeyboardMarkup(text='Подробнее', callback_data='desc2')
btns2 = InlineKeyboardMarkup(row_width=2).row(add_to_cart2, descriptona2)


add_to_cart3 = InlineKeyboardButton(text='Добавить в корзину: ', callback_data='add3')
descriptona3 = InlineKeyboardMarkup(text='Подробнее', callback_data='desc3')
btns3 = InlineKeyboardMarkup(row_width=2).row(add_to_cart3, descriptona3)


