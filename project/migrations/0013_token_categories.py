# Generated by Django 4.0.5 on 2022-09-17 13:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_blockchain_image_blockchain_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, help_text='Category', null=True, size=None, verbose_name='Category'),
        ),
    ]
