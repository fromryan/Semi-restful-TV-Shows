# Generated by Django 2.2 on 2020-02-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
