from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Company", callback_data="company"),
        InlineKeyboardButton(text="Individual", callback_data="individual")
    )
    return keyboard
