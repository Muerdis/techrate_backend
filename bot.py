import asyncio
import telegram

from django.conf import settings

settings.configure()


# async def main():
#     bot = telegram.Bot(settings.BOT_TOKEN)
#     async with bot:
#         print((await bot.get_updates())[2])


async def main():
    bot = telegram.Bot(settings.BOT_TOKEN)
    async with bot:
        await bot.send_message(text="Settings test", chat_id="-758645030")


if __name__ == '__main__':
    asyncio.run(main())
