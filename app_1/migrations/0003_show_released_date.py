# Generated by Django 2.2 on 2020-02-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_auto_20200219_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='released_date',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
