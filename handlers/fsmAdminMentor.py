from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup




class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
       await FSMAdmin.name.set()
       await  message.answer('Введите ID ментора')
    else:
        await message.answer('Пиши в группу')



async def load_id_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await FSMAdmin.next()
    await message.answer("Введите имя ментора")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.from_user.username
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направление?")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?")

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")
    elif int(message.text) < 16 or int(message.text) > 40:
        await message.answer("Возростное ограничение")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какая групаа?")

async def load_group(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")
    elif int(message.text) < 0 or int(message.text) > 99:
        await message.answer("Такой группы нет")
    else:
        async with state.proxy() as data:
            data['group'] = message.text
        await FSMAdmin.next()



def register_handlers_fsm_anketa(dp: Dispatcher):
    dp .register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id_mentor, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
