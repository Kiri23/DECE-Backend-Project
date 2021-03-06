# Generated by Django 2.1.7 on 2019-04-17 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_auto_20190417_1548'),
        ('profesor', '__latest__'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(help_text='El profesor del curso',
                                    on_delete=django.db.models.deletion.CASCADE, to='profesor.Profesor'),
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
