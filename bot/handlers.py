from aiogram import types
from aiogram.dispatcher import Dispatcher
from bot.keyboards import get_start_keyboard

async def start_command(message: types.Message):
    await message.answer(
        "Hello! Please choose who you are:",
        reply_markup=get_start_keyboard()
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])

async def process_callback(callback: types.CallbackQuery):
    if callback.data == "company":
        await callback.message.answer("You chose «Company».")
    elif callback.data == "individual":
        await callback.message.answer("You chose Individual.")
    await callback.answer()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_callback_query_handler(process_callback)