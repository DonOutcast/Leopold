import os
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from src.main import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from src.keyboards.markups import get_menu_markup, get_back_menu, get_leopold_markup


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
        m_path = os.path.abspath("first_help.mp3")
        with open(m_path, 'rb') as m_voice:
            await bot.send_voice(message.from_user.id, voice=m_voice, duration=26)
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

    @staticmethod
    async def cmd_reg(message: types.Message, state: FSMContext):
        # file_step_1 = open("stet_1" + message.from_user.id + ".json")
        await GrantsStates.first()
        async with state.proxy() as data:
            data['name_of_project'] = message.text
        await GrantsStates.next()
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_markup())
        await bot.send_message(message.from_user.id, "Введите имя для регестрации вашего проекта!",
                               reply_markup=get_back_menu())

    @staticmethod
    async def user_answer_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['region_of_project'] = message.text
            await GrantsStates.next()
            await message.answer("Регион реализации проекта")

    @staticmethod
    async def user_answer_2(callback: types.CallbackQuery, state: FSMContext):
        name = callback.data.split("_")[1]
        # async with state.proxy() as data:
        #     data['user_role'] = name
        # await Registration.next()
        # await bot.edit_message_text(
        #     chat_id=callback.message.chat.id,
        #     message_id=callback.message.message_id,
        #     text=callback.message.text,
        #     reply_markup=None)
        # print("in function")
        m_path = os.path.abspath("leopold_voices/first_help.mp3")
        m_tts_path = os.path.abspath("leopold_voices/tts.mp3")
        with open(m_path, 'rb') as m_voice:
            await bot.send_voice(callback.from_user.id, voice=m_voice, duration=14)
        with open(m_tts_path, 'rb') as m_voice:
            await bot.send_voice(callback.from_user.id, voice=m_voice, duration=14)
        await callback.message.answer("Ведите свой уникальный токен: ")

    def register_handlers_system(self):
        self.dp.register_message_handler(self.cmd_start, commands=["start"])
        self.dp.register_message_handler(self.cmd_cancel_registration, Text(equals="Вернуться в главное меню 📜"),
                                         state="*")
        self.dp.register_message_handler(self.cmd_reg, lambda message: "Регистрация гранта 🔐" in message.text,
                                         state=None)
        self.dp.register_callback_query_handler(self.user_answer_2, Text(startswith="leopold_"),
                                                state='*')
