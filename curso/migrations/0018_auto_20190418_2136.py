# Generated by Django 2.1.7 on 2019-04-18 21:36

import curso.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0017_remove_diasdelasemana_curso_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diasdelasemana',
            name='dias',
            field=models.CharField(default='', max_length=50, unique=True, validators=[curso.validators.validacion_dias_de_la_semana], verbose_name='Días'),
        ),
    ]
