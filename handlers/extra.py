from aiogram import types, Dispatcher
import random


async def bad_words_filter(message: types.Message):
    bad_words = ['html', 'js', 'css', 'жинди', 'дурак']
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"Не матерись {message.from_user.full_name}, "
                                 f"сам ты {word}")
            await message.delete()
            break

    if message.reply_to_message:
        await message.pin()


    if message.text.startswith('game'):
        animated_emojis = ['🎯','🎳','⚽️','🏀','🎰','🎲']
        random_emoji = random.choice(animated_emojis)
        await message.answer(random_emoji)
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
