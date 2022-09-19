# Generated by Django 4.0.5 on 2022-09-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_remove_token_category_alter_token_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='category',
            field=models.CharField(default='test', help_text='Category', max_length=250, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
