# Generated by Django 2.1.7 on 2020-01-14 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funny_pictures', '0010_auto_20200108_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=500)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
