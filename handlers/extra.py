from aiogram import types, Dispatcher
import random
from config import OPENAI_TOKEN
import openai

openai.api_key = OPENAI_TOKEN
async def bad_words_filter(message: types.Message):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. "
               "The assistant is helpful, creative, clever, and very friendly."
               "\n\nHuman: Hello, who are you?\nAI: "
               "I am an AI created by OpenAI."
               " How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.answer(response['choice'][0]['text'])



    if message.text.startswith('game'):
        animated_emojis = ['🎯','🎳','⚽️','🏀','🎰','🎲']
        random_emoji = random.choice(animated_emojis)
        await message.answer(random_emoji)




def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
