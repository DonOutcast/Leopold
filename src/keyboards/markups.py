from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_menu_markup() -> ReplyKeyboardMarkup:
    help_button = KeyboardButton("О себе 🆘")
    information_button = KeyboardButton('Информация ⚠️')
    registration_button = KeyboardButton('Регистрация гранта 🔐')
    keyboards_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards_menu.row(registration_button).row(help_button, information_button).add()

    return keyboards_menu


def get_back_menu() -> ReplyKeyboardMarkup:
    back_to_menu_button = KeyboardButton("Вернуться в главное меню 📜")
    back_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    back_menu_keyboard.add(back_to_menu_button)
    return back_menu_keyboard


def get_leopold_markup() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_start')
    return leopold_markup.add(leopold_start_button)


def get_leopold_answer_1() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_1')
    return leopold_markup.add(leopold_start_button)
