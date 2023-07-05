from django_tgbot.bot import AbstractTelegramBot
from django_tgbot.state_manager.state_manager import StateManager
from django_tgbot.types.update import Update
from . import bot_token
from .models import TelegramUser, TelegramChat, TelegramState
from game.models import Answer


class TelegramBot(AbstractTelegramBot):
    def __init__(self, token, state_manager):
        super(TelegramBot, self).__init__(token, state_manager)

    def get_db_user(self, telegram_id):
        return TelegramUser.objects.get_or_create(telegram_id=telegram_id)[0]

    def get_db_chat(self, telegram_id):
        return TelegramChat.objects.get_or_create(telegram_id=telegram_id)[0]

    def get_db_state(self, db_user, db_chat):
        return TelegramState.objects.get_or_create(telegram_user=db_user, telegram_chat=db_chat)[0]

    def pre_processing(self, update: Update, user, db_user, chat, db_chat, state):
        super(TelegramBot, self).pre_processing(update, user, db_user, chat, db_chat, state)

    def post_processing(self, update: Update, user, db_user, chat, db_chat, state):
        callback = update.get_callback_query()
        print(callback)
        if callback is not None:
            input_answer = Answer.objects.get(id=int(callback.get_data()))
            db_user.current_question_id = input_answer
            db_user.health += input_answer.health_change
            db_user.money += input_answer.money_change
            db_user.morality += input_answer.morality_change
            db_user.save()
        super(TelegramBot, self).post_processing(update, user, db_user, chat, db_chat, state)


def import_processors():
    from . import processors


state_manager = StateManager()
bot = TelegramBot(bot_token, state_manager)
import_processors()
