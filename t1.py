import asyncio
import logging
import time
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions


from config import *
from knopka import *
from korzina import Users


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# my_card = []
user_card = []
new_user = {}
new_user['card'] = user_card
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!',  '\nИспользуй /info, '
                        'чтобы узнать список доступных команд!', reply_markup=menu)
    user_id_ = message.from_user.id
    new_user[message.from_user.id] = Users(message.from_user.id)
    id_ = new_user [message.from_user.id]
    id_.user_id = user_id_
    id_.first_name = message.from_user.first_name
    print(id_)
    return id_


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    msg = text(bold('Вас приветствует интернет магазин Единоборств Drakula2kg!'
                    'Для дальнейшей работы ознакомтесь с пунктом "меню"'
                    'Бот создан благодаря знания полученным в INIT.KG, при повышении квалификации у Кирилла, и Эркин байке!'),
               )
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(content_types=['photo'])
async def get_photo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Фото передается в базу')
    print(msg)


@dp.message_handler()
async def menu32(msg: types.Message):
    if msg.text =='Меню':
        await bot.send_photo(msg.from_user.id, p1, 'Боксерские перчатки GREEN HILL (преффесиональные/спарринг) - 1500сом.',  reply_markup=btns1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, p2, 'Боксерские перчатки GREEN HILL (преффесиональные/спарринг) - 1500сом.',  reply_markup=btns2)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, p3, 'Боксерские перчатки TOPTEN (преффесиональные/спарринг) - 1500сом.',  reply_markup=btns3)

    elif msg.text == 'Корзина':
        await bot.send_message(msg.from_user.id, 'Ваша корзина: ')
        for element in user_card:
            await bot.send_message(msg.from_user.id, element)



@dp.callback_query_handler()
async def show_deck(call: types.CallbackQuery):
    msg = call.data
    if call.data == 'desc1':
        await bot.send_message(call.from_user.id, deks_text)

    elif call.data == "desc2":
        await bot.send_message(call.from_user.id, desk_text2)

    elif call.data == 'desc3':
        await bot.send_message(call.from_user.id, desk_text3)

    elif msg == "add1":
        new_user['card'].append('Боксерские перчатки GREEN HILL')

    elif msg == 'add2':
        new_user['card'].append('Боксерские перчатки GREEN HILL')

    elif msg == 'add3':
        new_user['card'].append('Боксерские перчатки EXCALIBUR')
print(new_user['card'])


if __name__ == '__main__':
    executor.start_polling(dp)

