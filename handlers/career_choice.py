from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keyboards.prof_keyboards import make_row_keyboard, make_profession_keyboard, make_grade_keyboard
from less3.keyboards.keyboards import main_menu_keyboard

router = Router()

available_jobs = [
    "Программист",
    "Дизайнер",
    "Маркетолог",
]

available_grades = ['Junior', 'Middle', 'Senior']

class ChoiceProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите профессию",
        reply_markup=make_profession_keyboard()
    )
    await state.set_state(ChoiceProfile.job)

@router.message(ChoiceProfile.job, F.text.in_(available_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        text="Выберите уровень",
        reply_markup=make_grade_keyboard()
    )
    await state.set_state(ChoiceProfile.grade)

@router.message(ChoiceProfile.job, F.text == "назад")
async def prof_chosen_incorrect(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите профессию",
        reply_markup=make_profession_keyboard()
    )

@router.message(ChoiceProfile.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        f"Ваша профессия: {user_data['profession']}\n"
        f"Ваш уровень: {message.text}",
        reply_markup=main_menu_keyboard()
    )
    await state.clear()

@router.message(ChoiceProfile.grade, F.text == "назад")
async def grade_back(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите профессию",
        reply_markup=make_profession_keyboard()
    )
    await state.set_state(ChoiceProfile.job)

@router.message(ChoiceProfile.grade, F.text == "выход")
async def exit_to_main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Главное меню:",
        reply_markup=main_menu_keyboard()
    )

@router.message(ChoiceProfile.job, F.text == "выход")
async def exit_to_main_menu_from_job(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Главное меню:",
        reply_markup=main_menu_keyboard()
    )

