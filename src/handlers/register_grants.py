import os
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from src.main import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from src.keyboards.markups import get_menu_markup, get_back_menu, get_leopold_markup, get_leopold_answer_1


class GrantsStates(StatesGroup):
    name_of_project = State()
    region_of_project = State()
    logo_of_project = State()
    # auth_of_project = State()
    # auth_number = State()
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
                                   sticker="CAACAgIAAxkBAANaY_Bg4_apRG4OO36MJgEEJhrh2joAAk4QAAK4U1FJCuXGk9prtrAuBA")
            return
        await state.finish()
        await message.answer('Вы вернулись в главное меню', reply_markup=get_menu_markup())
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAANaY_Bg4_apRG4OO36MJgEEJhrh2joAAk4QAAK4U1FJCuXGk9prtrAuBA")

    @staticmethod
    async def cmd_reg(message: types.Message):
        # file_step_1 = open("stet_1" + message.from_user.id + ".json")
        await GrantsStates.first()
        # async with state.proxy() as data:
        #     data['name_of_project'] = message.text
        # await GrantsStates.next()
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_markup())
        await bot.send_message(message.from_user.id, "Введите имя для регестрации вашего проекта!",
                               reply_markup=get_back_menu())

    @staticmethod
    async def user_answer_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name_of_project'] = message.text
            await GrantsStates.next()
            await message.answer("Регион реализации проекта")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_answer_1())

    @staticmethod
    async def user_answer_2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['region_of_project'] = message.text
            await GrantsStates.next()
            await message.answer("Логотип вашего проекта")

    @staticmethod
    async def user_answer_3(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['logo_of_project'] = message.photo[0].file_id
            await GrantsStates.next()
            await message.answer("Общая информация о проекте")

    @staticmethod
    async def user_answer_4(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['description_of_project'] = message.text
        await GrantsStates.next()
        await message.answer("Опыт руководителя проекта")

    @staticmethod
    async def user_answer_5(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_experience'] = message.text
        await GrantsStates.next()
        await message.answer("Описания функциоанла руководителя")

    @staticmethod
    async def user_answer_6(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_function'] = message.text
        await GrantsStates.next()
        await message.answer("Адрес регистрации руководителя проекта")

    @staticmethod
    async def user_answer_7(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['address_manager'] = message.text
        await GrantsStates.next()
        await message.answer("Ссылка на ваше резюме")

    @staticmethod
    async def user_answer_8(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['resume_manager'] = message.text
        await GrantsStates.next()
        await message.answer("Видео-визитка(ссылка на ролик на любом видеохостинге)")

    @staticmethod
    async def user_answer_9(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_link_video'] = message.text
        await state.finish()
        await message.answer("Вы успешно зарегестрировали грант")
        await message.answer_sticker(sticker="CAACAgIAAxkBAAP2Y_BulRlfTl0B55jHN5CU4-HJuNAAAsgRAAIV2ZlIt-U5Fr6t6couBA")



    @staticmethod
    async def user_answer_(callback: types.CallbackQuery, state: FSMContext):
        name = callback.data.split("_")[1]
        # async with state.proxy() as data:
        #     data['user_role'] = name
        # await Registration.next()
        # await bot.edit_message_text(
        #     chat_id=callback.message.chat.id,
        #     message_id=callback.message.message_id,
        #     text="t",
        #     reply_markup=None)
        await callback.message.answer_sticker(
            sticker="CAACAgIAAxkBAANSY_BgQw-sPsGhrx5lwatzgUAzrDEAAmgQAAKm-pFI2DyWQP_oN3YuBA")
        # m_path = os.path.abspath("leopold_voices/first_help.mp3")
        # m_tts_path = os.path.abspath("leo_" + name + ".mp3")
        m_tts_path = os.path.abspath("leopold_voices/tts.mp3")
        print(m_tts_path)
        # with open(m_path, 'rb') as m_voice:
        #     await bot.send_voice(callback.from_user.id, voice=m_voice, duration=14)
        with open(m_tts_path, 'rb') as m_voice:
            await bot.send_voice(callback.from_user.id, voice=m_voice, duration=14)

    @staticmethod
    async def get_id(message: types.Message):
        await bot.send_message(message.from_user.id, text=message)

    def register_handlers_system(self):
        self.dp.register_message_handler(self.cmd_start, commands=["start"])
        self.dp.register_message_handler(self.cmd_cancel_registration, Text(equals="Вернуться в главное меню 📜"),
                                         state="*")
        self.dp.register_message_handler(self.cmd_reg, lambda message: "Регистрация гранта 🔐" in message.text,
                                         state=None)
        self.dp.register_message_handler(self.user_answer_1, state=GrantsStates.name_of_project)
        self.dp.register_message_handler(self.user_answer_2, state=GrantsStates.region_of_project)
        self.dp.register_message_handler(self.user_answer_3, content_types=['photo'], state=GrantsStates.logo_of_project)
        self.dp.register_message_handler(self.user_answer_4, state=GrantsStates.description_of_project)
        self.dp.register_message_handler(self.user_answer_5, state=GrantsStates.manager_experience)
        self.dp.register_message_handler(self.user_answer_6, state=GrantsStates.manager_function)
        self.dp.register_message_handler(self.user_answer_7, state=GrantsStates.address_manager)
        self.dp.register_message_handler(self.user_answer_8, state=GrantsStates.resume_manager)
        self.dp.register_message_handler(self.user_answer_9, state=GrantsStates.manager_link_video)
        self.dp.register_callback_query_handler(self.user_answer_, Text(startswith="leopold_"),
                                                state='*')
        self.dp.register_message_handler(self.get_id, content_types=[ContentType.ANY])
