from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from io import BytesIO
from PIL import Image
from django.core.files import File
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=70)
    new_image = File(im_io, name=image.name)
    return new_image


@processor(state_manager, from_states=state_types.All)
def show_question(bot: TelegramBot, update: Update, state: TelegramState):
    user = state.telegram_user
    question = user.current_question
    keyboard = InlineKeyboardMarkup.a([
        [
            InlineKeyboardButton.a(text=str(x), callback_data=str(x.next_question.id))
        ] for x in question.answers.all() if x.is_visible(user.health, user.money, user.morality)
    ])
    if question.image is not None:
        result = bot.sendPhoto(update.get_chat().get_id(), photo=question.image,
                               caption=question.text+'\nЗдоровье:{}, Деньги:{}'.format(user.health, user.money),
                               reply_markup=keyboard, upload=True)
        print(result)
    else:
        bot.sendMessage(update.get_chat().get_id(),
                        question.text+'\nЗдоровье:{}, Деньги:{}'.format(user.health, user.money),
                        reply_markup=keyboard)
