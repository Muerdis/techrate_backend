# Generated by Django 4.0.5 on 2022-09-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_token_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='index',
            field=models.PositiveIntegerField(blank=True, help_text='Index', null=True, verbose_name='Index'),
        ),
    ]
