from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Question, Answer


class AnswerInLine(admin.StackedInline):
    model = Answer
    fk_name = 'question'
    fields = [
        ('text', 'next_question'),
        ('min_health', 'max_health', 'health_change'),
        ('min_money', 'max_money', 'money_change'),
        ('min_morality', 'max_morality', 'morality_change')
    ]
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInLine
    ]
