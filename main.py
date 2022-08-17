import telebot
from telebot import types
from API import API
import keys as kb
from functions import send_message
from database import save_user, check_user
# Создаем бота
bot = telebot.TeleBot(API)
# 2 клава

reply_markup = kb.mmain_m

count_answ = {}
count_right_answ = {}
# Команда start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    global count_right_answ
    global count_answ
    bot.send_message(message.chat.id, "Hello world!", reply_markup=reply_markup)
    # Получение сообщений от юзера
    count_right_answ[message.chat.id] = 0
    count_answ[message.chat.id] = 1


@bot.message_handler(content_types=['text'])
def handler(message):
    global count_right_answ
    global count_answ
    if message.text == "Пройти интервью":
        bot.send_message(message.chat.id, "Выберите позицию", reply_markup=kb.mm_get_positions)
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Hello world!", reply_markup=reply_markup)
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "Отлично!")
    if message.text == "Менеджер отдела проектные-продажи":
        bot.send_message(message.chat.id, "Подтвердите свое участие, как только вы нажмете начать интервью пройти его заново будет нельзя",
                         reply_markup=kb.confirm_keyboard)
    if message.text == "Отмена":
        bot.send_message(message.chat.id, "Выберите позицию", reply_markup=kb.mm_get_positions)
    if message.text == "Начать интервью":
        if check_user(message.chat.id):
            print(message.chat.id)
            otvet = types.InlineKeyboardMarkup(row_width=2)
            otvet.add(kb.button_h5, kb.button_l5)
            count_right_answ[message.chat.id] = 0
            count_answ[message.chat.id] = 1
            bot.send_message(message.chat.id, "Какой у вас опыт работы?", reply_markup=otvet)
        else:
            bot.send_message(message.chat.id, "Извините, вы уже проходили интервью!")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global count_right_answ
    global count_answ
    print(call.message.chat.id)
    try:
        if call.message:
            if call.data == "good_sql" and count_answ.get(call.message.chat.id) == 2:
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                bot.send_message(call.message.chat.id, "Сколько байтов в int?", reply_markup=kb.otvet3)
                count_right_answ[call.message.chat.id] = count_right_answ.get(call.message.chat.id, 0) + 1
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ[call.message.chat.id] = count_answ.get(call.message.chat.id, 0) + 1
            elif call.data == "bad_sql" and count_answ.get(call.message.chat.id) == 2:
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                bot.send_message(call.message.chat.id, "Сколько байтов в int?", reply_markup=kb.otvet3)
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ[call.message.chat.id] = count_answ.get(call.message.chat.id, 0) + 1
            elif call.data == "bad" and count_answ.get(call.message.chat.id) == 1:
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                bot.send_message(call.message.chat.id, "Знаешь SQL?", reply_markup=kb.otvet2)
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ[call.message.chat.id] = count_answ.get(call.message.chat.id, 0) + 1
            elif call.data == "good" and count_answ.get(call.message.chat.id) == 1:
                print(call.message.chat.id)
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                count_right_answ[call.message.chat.id] = count_right_answ.get(call.message.chat.id, 0) + 1
                bot.send_message(call.message.chat.id, "Знаешь SQL?", reply_markup=kb.otvet2)
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ[call.message.chat.id] = count_answ.get(call.message.chat.id, 0) + 1
            elif call.data == "good_q3_a2" and count_answ.get(call.message.chat.id) == 3:
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                count_right_answ[call.message.chat.id] = count_right_answ.get(call.message.chat.id, 0) + 1
                bot.send_message(call.message.chat.id, "Поздравляем вы прошли интервью", reply_markup=kb.mmain_m)
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ[call.message.chat.id] = count_answ.get(call.message.chat.id, 0) + 1
                save_user(call.message.chat.id)
                return
            elif (call.data == "bad_q3_a1" or call.data == "bad_q3_a3" or call.data == "bad_q3_a4") and \
                    count_answ.get(call.message.chat.id) == 3:
                bot.send_message(call.message.chat.id, "Следующий вопрос:")
                bot.send_message(call.message.chat.id, "Поздравляем вы прошли интервью", reply_markup=kb.mmain_m)
                bot.send_message(call.message.chat.id, count_right_answ[call.message.chat.id])
                count_answ += 1
                save_user(call.message.chat.id)
                return
        if count_right_answ[call.message.chat.id] >= 2:
            send_message()
    except Exception as e:
        print(repr(e))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
