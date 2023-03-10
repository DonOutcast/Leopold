from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_menu_markup() -> ReplyKeyboardMarkup:
    help_button = KeyboardButton("Леопольд 🦁")
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
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_start")
    return leopold_markup.add(leopold_start_button, leopold_question_button)


def get_leopold_answer_1() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_1')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_1")
    return leopold_markup.add(leopold_start_button, leopold_question_button)


def get_leopold_answer_2() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_2')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_2")
    return leopold_markup.add(leopold_start_button, leopold_question_button)


def get_leopold_answer_3() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_3')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_3")
    return leopold_markup.add(leopold_start_button, leopold_question_button)




def get_leopold_answer_4() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_4')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_4")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

def get_leopold_answer_5() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_5')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_5")
    return leopold_markup.add(leopold_start_button, leopold_question_button)


def get_leopold_answer_6() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_6')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_6")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

def get_leopold_answer_7() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_7')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_7")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

def get_leopold_answer_8() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_8')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_8")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

def get_leopold_answer_9() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_9')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_9")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

def get_leopold_answer_10() -> InlineKeyboardMarkup:
    leopold_markup = InlineKeyboardMarkup(row_width=1)
    leopold_start_button = InlineKeyboardButton(text="Позвать Леопольда 🦁", callback_data='leopold_10')
    leopold_question_button = InlineKeyboardButton(text="Спросить Леопольда 🦁", callback_data="question_10")
    return leopold_markup.add(leopold_start_button, leopold_question_button)

