# Generated by Django 2.1.7 on 2020-02-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0016_auto_20200216_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=500)),
                ('likes', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
    ]
