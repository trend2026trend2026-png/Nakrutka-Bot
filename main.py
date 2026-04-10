import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiohttp import web

# MA'LUMOTLAR
TOKEN = "8673795387:AAFioVGmoTAOXoO1CXxrpyhAoyYmtEXGkLg"
ADMIN_ID = 8308144667

bot = Bot(token=TOKEN)
dp = Dispatcher()

# RENDER SERVERI UCHUN
async def handle(request):
    return web.Response(text="Bot is Live!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# BOT BUYRUQLARI
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="➕ Xizmat qo'shish")],
        [types.KeyboardButton(text="📊 Statistika"), types.KeyboardButton(text="🔑 API sozlash")],
        [types.KeyboardButton(text="📩 Xabar yuborish"), types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("👋 Salom! Zento SMM botiga xush kelibsiz.", reply_markup=keyboard)

@dp.message(F.text == "📊 Statistika")
async def show_stats(message: types.Message):
    await message.answer("📈 Bot hozircha ishga tushdi!")

async def main():
    # Serverni fonda ishga tushirish
    asyncio.create_task(start_web_server())
    # Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
