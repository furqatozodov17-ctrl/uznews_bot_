import asyncio
from telegram import Bot

TOKEN = 8215679380:AAFaIdYt_YBad4wF49UI1R6EJQXzCHM8UUU
CHANNEL = "@xorezm_news_24"

bot = Bot(token=TOKEN)

async def main():
    while True:
        await bot.send_message(chat_id=CHANNEL, text="Salom! Bu test yangilik.")
        print("Xabar yuborildi ✅")
        await asyncio.sleep(900)  # har 15 daqiqada 1 marta

if name == "main":
    asyncio.run(main())
