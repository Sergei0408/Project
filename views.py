from django.conf import settings
import telebot
import settings
import os

TOKEN = settings.TELEGRAM_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, '''Здравствуйте, {0.first_name}!
{1.first_name} - бот для изучения иностранного языка. 
Давайте начнем!'''.format(message.from_user, bot.get_me()))


@bot.message_handler(content_types=['text'])
def dictionary(message):
    
    bot.register_next_step_handler(new_term, new_definition)
    term_works.write_term(new_term, new_definition)

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

bot.polling(none_stop=True)