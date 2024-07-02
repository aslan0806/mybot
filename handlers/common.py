from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.random_fox import fox
from less3.keyboards.keyboards import kb1, main_menu_keyboard
from random import randint

router = Router()

@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=main_menu_keyboard())

@router.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=main_menu_keyboard())

@router.message(Command("fox"))
@router.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)

@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")

@router.message(F.text == "выход")
@router.message(F.text == "назад")
@router.message(F.text == "В главное меню")
async def go_to_main_menu(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_menu_keyboard())

@router.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer("УРАААА!")
    elif message.text == "инфо":
        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)
