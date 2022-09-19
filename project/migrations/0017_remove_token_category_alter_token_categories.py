# Generated by Django 4.0.5 on 2022-09-19 11:14

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_token_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='category',
        ),
        migrations.AlterField(
            model_name='token',
            name='categories',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=250), help_text='Categories', size=None, verbose_name='Categories'),
        ),
    ]