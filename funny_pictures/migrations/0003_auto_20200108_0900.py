# Generated by Django 2.1.7 on 2020-01-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0002_auto_20200108_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(upload_to='pictures/'),
        ),
    ]
