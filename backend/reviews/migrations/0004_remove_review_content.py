# Generated by Django 3.1.1 on 2020-09-24 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200924_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
    ]
