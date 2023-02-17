import os
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from src.main import bot
from aiogram.dispatcher.filters.state import State, StatesGroup


# from prototype.basicui.keyboards.inline_kb import filter_drop_booking
# from prototype.basicui.keyboards.inline_kb import city_markup, users_markup
# from prototype.basicui.keyboards.system_kb import keyboards_menu, back_menu_keyboard

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


