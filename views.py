from django.conf import settings
import telebot
import settings
import os
import terms_work
from telebot import types

TOKEN = settings.TELEGRAM_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, '''Здравствуйте, {0.first_name}!
{1.first_name} - бот для изучения иностранного языка. 
Давайте начнем!'''.format(message.from_user, bot.get_me()))
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Записать слово", zapis)
    item2 = types.InlineKeyboardButton("Вспомнить слово", chtenie)
    markup.add(item1,item2)
    bot.send_message(message.chat.id, 'Начинаем', reply_markup=service)


@bot.message_handler(content_types=['text'])
def dictionary(message):
    '''
    dictionary(message)
    print(message)
    print(message.text)
    s = message.text.split(' - ')
    new_term = s[0]
    new_definition = s[1]
    print(s[1])
    terms_work.write_term(new_term, new_definition)
    print(message.text)
    qw = message.txt
    qw = qw.replac('=', '')
    terms = terms_work.get_terms_for_table()
    q = [i for i, (_, x, _) in enumerate(terms) if x == qw]
    print(q)
    bot.send_message(message.chat.id, terms[q][2])
    '''

    if '-' in message.text:
        dictionary(message)
        print(message)
        print(message.text)
        s = message.text.split(' - ')
        new_term = s[0]
        new_definition = s[1]
        print(s[1])
        terms_work.write_term(new_term, new_definition)

    elif '=' in message.text:
        print(message.text)
        qw = message.txt
        qw = qw.replac('=','')
        terms  = terms_work.get_terms_for_table()
        q = [i for i, (_, x, _) in enumerate(terms) if x == qw]
        print(q)
        bot.send_message(message.chat.id, terms[q][2])

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