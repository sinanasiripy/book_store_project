# Generated by Django 4.0.4 on 2022-04-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]
