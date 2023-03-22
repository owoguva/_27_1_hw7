from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from database.bot_dp import sql_command_random



# @dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://medialeaks.ru/wp-content/uploads/2022/11/snimok-ekrana-7545.jpg')
# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Вторая мировая война "
    answer = [
        "1939-1945",
        "1941-1945",
        "1916-1918",
        "1938-1945",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer(
        f"@{random_user[1]} {random_user[2]} {random_user[3]} {random_user[4]}\n"
                f"{random_user[5]}"
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_image, commands=['mem'])
    dp.register_message_handler(get_random_user, commands=['get'])
