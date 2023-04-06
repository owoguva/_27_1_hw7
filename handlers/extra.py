import openai
from aiogram import types, Dispatcher

from config import OPENAI_TOKEN


openai.api_key = OPENAI_TOKEN
async def bad_words_filter(message: types.Message):

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        await message.answer(response['choices'][0]['text'])

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter,commands=['go'], content_types=['text'])
