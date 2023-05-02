#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

'''
from telegram.ext import Updater
from telegram.ext import CommandHandler

def sms(manage, update):
    manage.message.reply_text('HHHH')

def func():
    my_bot = Updater('6193890914:AAGM8Su_8a752X3k4CUPZriG3FHemQ10FYk', 'https://web.telegram.org/k/#@lang_learn_1_bot', use_context = True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.start_pollyng()
    my_bot.idle()

func()
'''