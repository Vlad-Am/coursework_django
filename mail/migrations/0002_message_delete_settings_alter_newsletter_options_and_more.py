# Generated by Django 4.2 on 2024-04-02 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('subject', models.TextField(verbose_name='Тема письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='message',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='subject',
        ),
        migrations.AddField(
            model_name='client',
            name='newsletter',
            field=models.ManyToManyField(blank=True, to='mail.newsletter', verbose_name='Сообщения'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='datetime',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания рассылки'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default=None, max_length=10, verbose_name='Частота рассылки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default=None, max_length=10, verbose_name='Статус рассылки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mail.message', verbose_name='Сообщение'),
        ),
    ]
