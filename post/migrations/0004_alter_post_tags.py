# Generated by Django 4.0.5 on 2022-07-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Tags', to='post.tag', verbose_name='Tags'),
        ),
    ]
