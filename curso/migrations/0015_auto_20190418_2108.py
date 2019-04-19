# Generated by Django 2.1.7 on 2019-04-18 21:08

import curso.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0014_auto_20190418_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasDeLaSemana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.CharField(default='', max_length=50, validators=[curso.validators.validacion_dias_de_la_semana], verbose_name='Días')),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='dias',
        ),
        migrations.AddField(
            model_name='curso',
            name='dias',
            field=models.ManyToManyField(to='curso.DiasDeLaSemana', verbose_name='Días'),
        ),
    ]
