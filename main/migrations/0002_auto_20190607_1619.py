# Generated by Django 2.2.1 on 2019-06-07 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='ip',
        ),
    ]