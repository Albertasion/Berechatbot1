from aiogram import executor
from mysql_connect import mycursor, mydb
from query_categories import *
from query_list import *
from config import BASE_URL_CATEGORY
from dispatch import dp
from aiogram import types


mycursor.execute(res)
rows = mycursor.fetchall()
for row in rows:
   category_id.append(row[0])
   query_category_names_main.append(row[25])
   query_category_links.append(row[10])
mycursor.execute(res2)
rows2 = mycursor.fetchall()
for row in rows2:
    sub_categories.append(row[1])
mydb.commit()
mydb.close()
del query_category_names_main [-1]
for i in query_category_links:
    i=BASE_URL_CATEGORY+i
    res_category_links_url.append(i)


print(sub_categories)
print(query_category_links)
print(query_category_names_main)
print(category_id)
print(res_category_links_url)
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)