# Generated by Django 2.1.7 on 2020-02-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
    ]