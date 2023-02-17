import os
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from src.main import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from src.keyboards.markups import get_menu_markup, get_back_menu


class GrantsStates(StatesGroup):
    name_of_project = State()
    region_of_project = State()
    logo_of_project = State()
    auth_of_project = State()
    auth_number = State()
    description_of_project = State()
    manager_experience = State()
    manager_function = State()
    address_manager = State()
    resume_manager = State()
    manager_link_video = State()


class RegisterGrant:

    def __init__(self, dp):
        self.dp = dp

    @staticmethod
    async def cmd_start(message: types.Message):
        path = os.path.abspath('images/title.jpeg')
        with open(path, 'rb') as photo:
            await bot.send_photo(message.from_user.id,
                                 photo=photo)
        await bot.send_message(message.from_user.id, "Добро пожаловать!\nЗдесь вы можете сделать совй грант",
                               reply_markup=get_menu_markup())
        await message.delete()

    @staticmethod
    async def cmd_cancel_registration(message: types.Message, state: FSMContext):
        await message.delete()
        try:
            await bot.delete_message(message.from_user.id, message_id=message.message_id - 1)
        except:
            pass
        current_state = await state.get_state()
        if current_state is None:
            await message.answer('Вы вернулись в главное меню', reply_markup=get_menu_markup())
            await bot.send_sticker(message.from_user.id,
                                   sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")
            return
        await state.finish()
        await message.answer('Вы вернулись в главное меню', reply_markup=get_menu_markup())
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAENm1Bi_0Q9YClvUdjgvDLx0S5V3Z3UUgAClgcAAmMr4glEcXCvl0uDLSkE")

    def register_handlers_system(self):
        self.dp.register_message_handler(self.cmd_start, commands=["start"])
        # self.dp.register_message_handler(self.cmd_cancel_registration, Text(equals="Вернуться в главное меню 📜"),
        #                                  state="*")
