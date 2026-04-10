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

# --- RENDER SERVERI ---
async def handle(request):
    return web.Response(text="Sacury SMM is Running Like Seen.uz")

async def start_web():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# --- KLAVIATURA (Seen.uz uslubida) ---
def main_menu():
    kb = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="💰 Balansni to'ldirish"), types.KeyboardButton(text="👤 Kabinet")],
        [types.KeyboardButton(text="📊 Buyurtmalarim"), types.KeyboardButton(text="🆘 Yordam")],
    ]
    if ADMIN_ID == 8308144667: # Admin uchun qo'shimcha tugma
         kb.append([types.KeyboardButton(text="⚙️ Admin Panel")])
    
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# --- BOT FUNKSIYALARI ---

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer(
        f"👋 Salom {msg.from_user.first_name}!\n\n"
        "**Sacury SMM** (Zento) botiga xush kelibsiz. "
        "Bu yerda siz ijtimoiy tarmoqlar uchun sifatli nakrutka xizmatlaridan foydalanishingiz mumkin.",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "🛍 Buyurtma berish")
async def order(msg: types.Message):
    # Bu yerda Seen.uz dagi kabi kategoriyalar chiqadi
    await msg.answer("👇 Iltimos, xizmat turini tanlang:\n\n1. Instagram 📸\n2. Telegram ✈️\n3. TikTok 🎵\n4. YouTube 🎥")

@dp.message(F.text == "💰 Balansni to'ldirish")
async def refill(msg: types.Message):
    await msg.answer(
        "💰 Balansni to'ldirish usulini tanlang:\n\n"
        "💳 **Click / Payme** (Avtomatik)\n"
        "👤 **Admin orqali** (Check yuborish)",
        parse_mode="Markdown"
    )

@dp.message(F.text == "👤 Kabinet")
async def cabinet(msg: types.Message):
    await msg.answer(
        f"👤 **Sizning ma'lumotlaringiz:**\n\n"
        f"🆔 ID: `{msg.from_user.id}`\n"
        f"💰 Balans: `0.00 so'm`\n"
        f"📊 Jami buyurtmalar: `0 ta`",
        parse_mode="Markdown"
    )

# --- ISHGA TUSHIRISH ---
async def main():
    asyncio.create_task(start_web())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
