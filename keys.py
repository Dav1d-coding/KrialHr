from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

mmain_m = types.ReplyKeyboardMarkup(row_width=2)
button1 = types.KeyboardButton("Пройти интервью")
button2 = types.KeyboardButton(" Как дела?")
mmain_m.add(button1, button2)

mm_get_positions = types.ReplyKeyboardMarkup(row_width=3)
button_saler = types.KeyboardButton("Продажник")
button_project = types.KeyboardButton("Проектник")
button_proger = types.KeyboardButton("Менеджер отдела проектные-продажи")
button_back = types.KeyboardButton("Назад")
button_yes = types.InlineKeyboardButton("Да", callback_data='good_sql')
button_no = types.InlineKeyboardButton("Нет", callback_data='bad_sql')
mm_get_positions.add(button_proger, button_back)

confirm_keyboard = types.ReplyKeyboardMarkup(row_width=2)
button_confirm = types.KeyboardButton("Начать интервью")
button_cancel = types.KeyboardButton("Отмена")
confirm_keyboard.add(button_confirm, button_cancel)

button_l5 = types.InlineKeyboardButton("<5 лет", callback_data='bad', one_time_keybord='true')
button_h5 = types.InlineKeyboardButton(">5 лет", callback_data='good')

otvet2 = types.InlineKeyboardMarkup(row_width=2)
otvet2.add(button_yes, button_no)

button_b5 = types.InlineKeyboardButton("5", callback_data='bad_q3_a1')
button_b4 = types.InlineKeyboardButton("4", callback_data='good_q3_a2')
button_b3 = types.InlineKeyboardButton("3", callback_data='bad_q3_a3')
button_b2 = types.InlineKeyboardButton("2", callback_data='bad_q3_a4')

otvet3 = types.InlineKeyboardMarkup(row_width=4)
otvet3.add(button_b5, button_b4, button_b3, button_b2)
