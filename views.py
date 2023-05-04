from django.conf import settings
import telebot
import settings
import os
import terms_work
from telebot import types
import time

TOKEN = settings.TELEGRAM_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, '''Здравствуйте, {0.first_name}!
{1.first_name} - бот для изучения иностранного языка. 
Давайте начнем!'''.format(message.from_user, bot.get_me()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Запомнить слово")
    item2 = types.KeyboardButton("Вспомнить слово")
    markup.add(item1,item2)

    bot.send_message(message.chat.id, "Начали".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)
   # bot.send_message(message.chat.id, 'Начинаем', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dictionary(message):
    print(message.text)
    sms = message.text
    if sms == 'Запомнить слово':
        bot.send_message(message.chat.id, "Введите определение через знак -")
    elif sms == 'Вспомнить слово':
        bot.send_message(message.chat.id, "Введите слово и добавьте знак вопроса (в формате: слово? )")
    elif sms == "Записать время занятия":
        seconds = time.time()
        local_time = time.ctime(seconds)
        terms_work.write_date(local_time)
    elif sms == "Просмотреть время занятий":
        date = terms_work.get_date_for_table()
        all_time = []
        for x in date:
            all_time.append(x[1])
        bot.send_message(message.chat.id, "\n".join(all_time))
    elif '-' in sms:
        s = sms.split(' - ')
        new_term = s[0].lower()
        new_definition = s[1].lower()
        terms_work.write_term(new_term, new_definition)
        bot.send_message(message.chat.id, "Выберите следующее действие")
    elif '?' in sms:
        qw = sms.replace('?','').lower()
        terms  = terms_work.get_terms_for_table()
        print(qw)
        q = [i for i, (_, x, _) in enumerate(terms) if x == qw]
        try:
            n = int(q[0])
            print(terms[n][2])
            bot.send_message(message.chat.id, terms[n][2])
        except Exception as e:
            bot.send_message(message.chat.id, 'Такого слова в словаре нет')

    else:
        bot.send_message(message.chat.id, 'Неизвестный запрос')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Запомнить слово")
    item2 = types.KeyboardButton("Вспомнить слово")
    item3 = types.KeyboardButton("Записать время занятия")
    item4 = types.KeyboardButton("Просмотреть время занятий")
    markup.add(item1, item2)
    markup.add(item3, item4)

    if '-' not in sms and sms !='Вспомнить слово' and sms !='Запомнить слово':
        bot.send_message(message.chat.id, "Выберите следующее действие".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)
'''
@bot.message_handler(func=lambda message: message == "действие")
def reply_message_handler(message):
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)
'''

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.message:
            if call.data == 'zapis':
                bot.send_message(call.message.chat.id, 'Запишите слово и определение через знак -')
            elif call.data == 'chtenie':
                bot.send_message(call.message.chat.id, 'Какое слово Вы ищите? Воспользуйтесь знаком = ')

'''
from django.core.exceptions import PermissionDenied

def bothook(request):
    if request.META["CONTENT_TYPE"] == "application/json": #проверка на то, какого типа пришел запрос
        json_data = request.body.decode("utf-8")
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse("")
    else:
        raise PermissionDenied  # ошибка 403. Мы таким образом защищаем бота от разнообразных атак.
'''

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)