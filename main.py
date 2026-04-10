import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiohttp import web

# MA'LUMOTLAR
TOKEN = "8673795387:AAFioVGmoTAOXoO1CXxrpyhAoyYmtEXGkLg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# RENDER SERVERI (Bot o'chib qolmasligi uchun)
async def handle(request):
    return web.Response(text="Zento SMM is Running!")

async def start_web():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# ASOSIY MENYU
def get_main_kb():
    buttons = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="💰 Balans"), types.KeyboardButton(text="👤 Kabinet")],
        [types.KeyboardButton(text="📊 Buyurtmalarim"), types.KeyboardButton(text="🆘 Yordam")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"👋 Salom {message.from_user.first_name}!\n\n"
        "🚀 **Zento SMM** botiga xush kelibsiz.\n"
        "Ijtimoiy tarmoqlarda sifatli rivojlanishni biz bilan boshlang!",
        reply_markup=get_main_kb(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "💰 Balans")
async def balance_cmd(message: types.Message):
    await message.answer("💰 Sizning balansingiz: **0.00 so'm**\n\nBalansni to'ldirish uchun adminga murojaat qiling.", parse_mode="Markdown")

@dp.message(F.text == "👤 Kabinet")
async def kabinet_cmd(message: types.Message):
    text = (f"👤 **Kabinet ma'lumotlari:**\n\n"
            f"🆔 ID: `{message.from_user.id}`\n"
            f"💰 Balans: `0.00 so'm`\n"
            f"📊 Buyurtmalar: `0 ta` status")
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🛍 Buyurtma berish")
async def order_cmd(message: types.Message):
    await message.answer("👇 **Xizmat turini tanlang:**\n\n1. Telegram ✈️\n2. Instagram 📸\n3. TikTok 🎵\n4. YouTube 🎥", parse_mode="Markdown")

async def main():
    asyncio.create_task(start_web())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
