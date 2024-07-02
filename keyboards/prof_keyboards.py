from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def make_row_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

def make_profession_keyboard() -> ReplyKeyboardMarkup:
    buttons = ["Программист", "Дизайнер", "Маркетолог", "назад", "выход"]
    return make_row_keyboard(buttons)

def make_grade_keyboard() -> ReplyKeyboardMarkup:
    buttons = ["Junior", "Middle", "Senior", "назад", "выход"]
    return make_row_keyboard(buttons)
