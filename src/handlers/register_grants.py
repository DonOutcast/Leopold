import os
import json
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from main import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.markups import get_menu_markup, get_back_menu, get_leopold_markup, get_leopold_answer_1, \
    get_leopold_answer_2, get_leopold_answer_3, get_leopold_answer_4, get_leopold_answer_5


class GrantsStates(StatesGroup):
    name_of_project = State()
    region_of_project = State()
    logo_of_project = State()
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
        path = os.path.abspath('images/title.png')
        with open(path, 'rb') as photo:
            await bot.send_photo(message.from_user.id,
                                 photo=photo)
        await bot.send_message(message.from_user.id, "Добро пожаловать!\nЗдесь вы можете сделать совй грант",
                               reply_markup=get_menu_markup())
        await message.delete()

    @staticmethod
    async def cmd_info_leopold(message: types.Message):
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAIBgGPwrk8EvM7uDdjEwB_-0rOUbrUhAAIlDwACS5ORSOscHL4fo5kKLgQ",
                               reply_markup=get_leopold_markup())

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
        await bot.send_message(message.from_user.id, "Введите имя для регестрации вашего проекта!",
                               reply_markup=get_back_menu())
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_answer_1())

    @staticmethod
    async def user_answer_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name_of_project'] = message.text
            await GrantsStates.next()
            await message.answer("Укажите регион реализации проекта.")
        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAICLGPw_oj4QJwM6qyfUKH2AAFGWN-aigACw8IxG85-iUs2ycnEtkNDowEAAwIAA3kAAy4E",
                             reply_markup=get_leopold_answer_2())

    @staticmethod
    async def user_answer_2(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['region_of_project'] = message.text
            await GrantsStates.next()
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAICRWPxAAHaqbL7kMO5Bd1gzPPnASSARQAChyUAAs5-iUvaIQGVdXUjTy4E",
                               reply_markup=get_leopold_answer_3())
        await message.answer("Логотип вашего проекта")


    @staticmethod
    async def user_answer_3(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['logo_of_project'] = message.photo[0].file_id
            await GrantsStates.next()
            await message.answer("Общая информация о проекте")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_answer_4())

    @staticmethod
    async def user_answer_4(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['description_of_project'] = message.text
        await GrantsStates.next()
        await message.answer("Опыт руководителя проекта")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAICcmPxA2jkWcLb-C_lbO7YGcIW8b69AAKlJQACzn6JS_ibAYcTOs9cLgQ",
                               reply_markup=get_leopold_answer_4()
                               )

    @staticmethod
    async def user_answer_5(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_experience'] = message.text
        await GrantsStates.next()
        await message.answer("Описания функциоанла руководителя")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               reply_markup=get_leopold_answer_5())

    @staticmethod
    async def user_answer_6(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_function'] = message.text
        await GrantsStates.next()
        await message.answer("Адрес регистрации руководителя проекта")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               )

    @staticmethod
    async def user_answer_7(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['address_manager'] = message.text
        await GrantsStates.next()
        await message.answer("Ссылка на ваше резюме")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               )

    @staticmethod
    async def user_answer_8(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['resume_manager'] = message.text
        await GrantsStates.next()
        await message.answer("Видео-визитка(ссылка на ролик на любом видеохостинге)")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               )

    @staticmethod
    async def user_answer_9(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['manager_link_video'] = message.text
        await state.finish()
        await message.answer("Вы успешно зарегестрировали грант")
        await message.answer_sticker(sticker="CAACAgIAAxkBAAP2Y_BulRlfTl0B55jHN5CU4-HJuNAAAsgRAAIV2ZlIt-U5Fr6t6couBA")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgEAAxkBAAENoVljAh8xTOx1Nmxyk4ruq8V7cITCYQAC7AcAAuN4BAAB6DEEbU_xFOwpBA",
                               )

    @staticmethod
    async def leopold_voice(callback: types.CallbackQuery):
        name = callback.data.split("_")[1]
        await callback.message.answer_sticker(
            sticker="CAACAgIAAxkBAANSY_BgQw-sPsGhrx5lwatzgUAzrDEAAmgQAAKm-pFI2DyWQP_oN3YuBA")
        m_tts_path = os.path.abspath("leo_" + name + ".mp3")
        with open(m_tts_path, 'rb') as m_voice:
            await bot.send_voice(callback.from_user.id, voice=m_voice, duration=14)

    @staticmethod
    async def leopold_question(callback: types.CallbackQuery):
        with open("dataset/question.json", "r") as dataset:
            data = json.load(dataset)
        name = callback.data.split("_")[1]
        await callback.message.answer_sticker(
            sticker="CAACAgIAAxkBAAIBaWPwrA89ykFxTaXNBG_gNSfBl_GgAAJgEgACM0iQSEF3NGa0-C4JLgQ")
        await bot.send_message(callback.from_user.id, text=data.get(name))

    @staticmethod
    async def get_id(message: types.Message):
        await bot.send_message(message.from_user.id, text=message)

    def register_handlers_system(self):
        self.dp.register_message_handler(self.cmd_start, commands=["start"])
        self.dp.register_message_handler(self.cmd_cancel_registration, Text(equals="Вернуться в главное меню 📜"),
                                         state="*")
        self.dp.register_message_handler(self.cmd_reg, lambda message: "Регистрация гранта 🔐" in message.text,
                                         state=None)
        self.dp.register_message_handler(self.cmd_info_leopold, lambda message: "Леопольд 🦁" in message.text,
                                         state=None)
        self.dp.register_message_handler(self.user_answer_1, state=GrantsStates.name_of_project)
        self.dp.register_message_handler(self.user_answer_2, state=GrantsStates.region_of_project)
        self.dp.register_message_handler(self.user_answer_3, content_types=['photo'],
                                         state=GrantsStates.logo_of_project)
        self.dp.register_message_handler(self.user_answer_4, state=GrantsStates.description_of_project)
        self.dp.register_message_handler(self.user_answer_5, state=GrantsStates.manager_experience)
        self.dp.register_message_handler(self.user_answer_6, state=GrantsStates.manager_function)
        self.dp.register_message_handler(self.user_answer_7, state=GrantsStates.address_manager)
        self.dp.register_message_handler(self.user_answer_8, state=GrantsStates.resume_manager)
        self.dp.register_message_handler(self.user_answer_9, state=GrantsStates.manager_link_video)
        self.dp.register_callback_query_handler(self.leopold_voice, Text(startswith="leopold_"),
                                                state='*')
        self.dp.register_callback_query_handler(self.leopold_question, Text(startswith="question_"),
                                                state='*')
        self.dp.register_message_handler(self.get_id, content_types=[ContentType.ANY])
