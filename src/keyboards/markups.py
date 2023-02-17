from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, WebAppInfo


def get_menu_markup() -> ReplyKeyboardMarkup:
    help_button = KeyboardButton("О себе 🆘")
    information_button = KeyboardButton('Информация ⚠️')
    registration_button = KeyboardButton('Регистрация гранта 🔐')
    booking_button = KeyboardButton('Бронирование ✅')
    my_bookings_button = KeyboardButton('Мои брони 📝')
    admin_button = KeyboardButton('Добавить объект 👨🏻‍💻')
    keyboards_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards_menu.row(registration_button, admin_button).row(booking_button, my_bookings_button).row(help_button,
                                                                                                      information_button).add()

    return keyboards_menu


def get_back_menu() -> ReplyKeyboardMarkup:
    back_to_menu_button = KeyboardButton("Вернуться в главное меню 📜")
    back_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    back_menu_keyboard.add(back_to_menu_button)
    return back_menu_keyboard
