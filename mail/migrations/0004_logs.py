# Generated by Django 4.2 on 2024-04-11 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_last_send', models.DateTimeField(auto_now=True, verbose_name='Дата и время последней попытки')),
                ('status', models.TextField(verbose_name='Статус')),
                ('answer', models.TextField(verbose_name='Ответ сервера')),
                ('newsletter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mail.newsletter', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Логи',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
