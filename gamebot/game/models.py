from django.db import models


class Question(models.Model):
    header = models.CharField(max_length=200, verbose_name='Заголовок вопроса')
    text = models.TextField(verbose_name='Текст вопроса')
    image = models.ImageField(verbose_name='Иллюстрация', blank=True, null=True)

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

    def __str__(self):
        return self.header


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    text = models.TextField()
    min_health = models.IntegerField(default=0, verbose_name='Минимальное здоровье')
    max_health = models.IntegerField(default=9, verbose_name='Максимальное здоровье')
    min_money = models.IntegerField(default=0, verbose_name='Минимальные деньги')
    max_money = models.IntegerField(default=9, verbose_name='Максимальные деньги')
    min_morality = models.IntegerField(default=0, verbose_name='Минимальная нравственность')
    max_morality = models.IntegerField(default=9, verbose_name='Максимальная нравственность')
    health_change = models.IntegerField(default=0, verbose_name='Изменение здоровья')
    money_change = models.IntegerField(default=0, verbose_name='Изменение денег')
    morality_change = models.IntegerField(default=0, verbose_name='Изменение нравственности')
    next_question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                      null=True, blank=True, related_name='previous', verbose_name='Следующий вопрос')

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'

    def __str__(self):
        return self.text


class Player(models.Model):
    telegram_chat_id = models.CharField(max_length=200, verbose_name='ID чата Telegram')
    current_question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Текущий вопрос')
    health = models.IntegerField(default=5, verbose_name='Здоровье')
    money = models.IntegerField(default=5, verbose_name='Деньги')
    morality = models.IntegerField(default=5, verbose_name='Нравственность')

    class Meta:
        verbose_name='Участник'
        verbose_name_plural='Участники'

    def __str__(self):
        return self.text