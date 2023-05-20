# Generated by Django 4.2.1 on 2023-05-20 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_chat_id', models.CharField(max_length=200, verbose_name='ID чата Telegram')),
                ('health', models.IntegerField(default=5, verbose_name='Здоровье')),
                ('money', models.IntegerField(default=5, verbose_name='Деньги')),
                ('morality', models.IntegerField(default=5, verbose_name='Нравственность')),
                ('current_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.question', verbose_name='Текущий вопрос')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]