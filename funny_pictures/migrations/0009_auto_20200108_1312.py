# Generated by Django 2.1.7 on 2020-01-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0008_auto_20200108_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.CharField(default='none', max_length=300),
        ),
    ]
