import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiohttp import web

# --- MA'LUMOTLAR ---
TOKEN = "8673795387:AAFioVGmoTAOXoO1CXxrpyhAoyYmtEXGkLg"
ADMIN_ID = 8308144667

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- RENDER UCHUN VEB-SERVER ---
async def handle(request):
    return web.Response(text="Sacury SMM boti faol!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# --- BOT BUYRUQLARI ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Salom! Sacury SMM botiga xush kelibsiz.\nBot 24/7 ishlamoqda.")

@dp.message(Command("admin"))
async def admin_cmd(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🛠 Xush kelibsiz, Admin!")
    else:
        await message.answer("❌ Siz admin emassiz.")

async def main():
    asyncio.create_task(start_web_server())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
