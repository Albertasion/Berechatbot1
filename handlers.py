from aiogram import types
from query_list import *
from dispatch import dp

#каталог главный кнопки
@dp.message_handler(commands="catalog")
async def cmd_catalog(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = query_category_names_main
    keyboard.add(*buttons)
    await message.answer("вібери", reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text == query_category_names_main[0])
    async def shows_generator(message: types.Message):
        await message.answer(f"Вы выбрали раздел: {query_category_names_main[0]} {res_category_links_url[0]}")


    @dp.message_handler(lambda message: message.text == query_category_names_main[1])
    async def shows_generator(message: types.Message):
        await message.answer(f"Вы выбрали раздел: {query_category_names_main[1]} {res_category_links_url[1]}")

    @dp.message_handler(lambda message: message.text == query_category_names_main[2])
    async def shows_generator(message: types.Message):
        await message.answer(f"Вы выбрали раздел: {query_category_names_main[2]} {res_category_links_url[2]}")

    @dp.message_handler(lambda message: message.text == query_category_names_main[3])
    async def shows_generator(message: types.Message):
        await message.answer(f"Вы выбрали раздел: {query_category_names_main[3]} {res_category_links_url[3]}")

#
# @dp.message_handler()
# async def echo(message: types.Message):
#     for i in message.text:
#         await message.answer(i)


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi!\nI'm EchoBot!")