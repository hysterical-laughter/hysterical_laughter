# Generated by Django 2.1.7 on 2020-02-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0017_auto_20200216_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.CharField(default='[]', max_length=10000),
        ),
    ]
