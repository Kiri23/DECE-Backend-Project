# Generated by Django 2.1.7 on 2019-04-19 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0020_auto_20190419_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtemas',
            name='curso',
        ),
    ]
