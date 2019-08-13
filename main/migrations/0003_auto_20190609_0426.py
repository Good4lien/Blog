# Generated by Django 2.2.1 on 2019-06-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190607_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Follow', 'verbose_name_plural': 'Followers'},
        ),
        migrations.AddField(
            model_name='follow',
            name='ip',
            field=models.GenericIPAddressField(default='0.0.0.0', unpack_ipv4=True),
            preserve_default=False,
        ),
    ]