# Generated by Django 2.1.7 on 2020-02-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0018_auto_20200217_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.CharField(max_length=10000),
        ),
    ]
