from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.bot_dp import sql_command_all_id
from apscheduler.triggers.cron import CronTrigger
from config import bot, ADMINS


async def happy_birthday(bot: Bot):
    user_ids = await sql_command_all_id()
    for user_id in user_ids:
        await bot.send_message(user_id[0], "Happy Birthday!")


async def send_message_date(bot: Bot):
    await bot.send_message(ADMINS[0], "DATE TRIGGER!")

async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(
        happy_birthday,
        trigger=CronTrigger(month=2, day=25, hour=1, minute=1),
        kwargs={"bot": bot}
    )

    scheduler.start()