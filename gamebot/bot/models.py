from django.db import models
from django.db.models import CASCADE
from game.models import Question

from django_tgbot.models import AbstractTelegramUser, AbstractTelegramChat, AbstractTelegramState


class TelegramUser(AbstractTelegramUser):
    current_question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1, verbose_name='Текущий вопрос')
    health = models.IntegerField(default=5, verbose_name='Здоровье')
    money = models.IntegerField(default=5, verbose_name='Деньги')
    morality = models.IntegerField(default=5, verbose_name='Нравственность')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.username


class TelegramChat(AbstractTelegramChat):
    pass


class TelegramState(AbstractTelegramState):
    telegram_user = models.ForeignKey(TelegramUser, related_name='telegram_states', on_delete=CASCADE, blank=True, null=True)
    telegram_chat = models.ForeignKey(TelegramChat, related_name='telegram_states', on_delete=CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ('telegram_user', 'telegram_chat')

