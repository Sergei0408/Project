from django.conf import settings
import telebot
import env
#TOKEN = settings.TELEGRAM_API_TOKEN

bot = telebot.TeleBot(env.TELEGRAM_API_TOKEN)

@bot.message_handler(commands=["text"])
def greet(message):
    bot.send_message(message.chat.id, 'message.text')

'''
from django.core.exceptions import PermissionDenied

 #декоратор csrf – cross site reference cooky, обеспечивает дополнительную безопасность
def bothook(request):
    if request.META["CONTENT_TYPE"] == "application/json": #проверка на то, какого типа пришел запрос
        json_data = request.body.decode("utf-8")
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse("") #после того, как все обработали,возвращаем пустой элемент. В рамках клиент-серверной архитектуры нужно
    else:
        raise PermissionDenied  # ошибка 403. Мы таким образом защищаем бота от разнообразных атак.
'''
bot.polling(none_stop = True)