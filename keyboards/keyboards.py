from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define buttons
button1 = KeyboardButton(text='/start')
button2 = KeyboardButton(text='/ура')
button3 = KeyboardButton(text='инфо')
button4 = KeyboardButton(text='/fox')
button5 = KeyboardButton(text='num')
button6 = KeyboardButton(text='/prof')

# Define keyboard layouts
keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6]
]

# Create ReplyKeyboardMarkup objects
kb1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return kb1
