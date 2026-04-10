import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiohttp import web

TOKEN = "8673795387:AAFioVGmoTAOXoO1CXxrpyhAoyYmtEXGkLg"
ADMIN_ID = 8308144667

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- SERVER QISMI ---
async def handle(request):
    return web.Response(text="Bot ishlayapti!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# --- ADMIN KLAVIATURASI ---
def get_admin_keyboard():
    kb = [
        [types.KeyboardButton(text="➕ Xizmat qo'shish")],
        [types.KeyboardButton(text="📊 Statistika"), types.KeyboardButton(text="🔑 API sozlash")],
        [types.KeyboardButton(text="📩 Xabar yuborish"), types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# --- BOT MANTIQI ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Salom! Zenta SMM botiga xush kelibsiz🤝\nBot 24/7 ishlamoqda.",
        reply_markup=get_admin_keyboard() if message.from_user.id == ADMIN_ID else None
    )

# TUGMALAR UCHUN JAVOBLAR:
@dp.message(F.text == "➕ Xizmat qo'shish")
async def add_service(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🛠 Yangi xizmat qo'shish bo'limi hali tayyor emas, lekin tugma ishladi!")

@dp.message(F.text == "📊 Statistika")
async def show_stats(message: types.Message):
    await message.answer("📈 Hozircha botda 1 ta foydalanuvchi bor (Siz).")

@dp.message(F.text == "🔑 API sozlash")
async def set_api(message: types.Message):
    await message.answer("🔑 SMM Panel API ID raqamini kiriting:")

async def main():
    asyncio.create_task(start_web_server())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
