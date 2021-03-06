# Generated by Django 2.1.7 on 2019-04-03 23:43

import curso.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(verbose_name='descripción')),
                ('dias', models.CharField(default='', max_length=50, validators=[curso.validators.validacion_dias_de_la_semana], verbose_name='Días')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cupos', models.PositiveSmallIntegerField(help_text='Los cupos disponibles para el curso')),
                ('duracion', models.PositiveSmallIntegerField(help_text='La duración del curso en horas', verbose_name='duración')),
                ('tieneSeccion', models.BooleanField(default=False, help_text='Marque el encasillado si este curso tiene una sección', verbose_name='tiene sección')),
                ('seccion', models.SlugField(blank=True, help_text='La sección del curso si este lleva una sección.')),
                ('categoria', models.ForeignKey(help_text='La categoria que pertenece este curso.', on_delete=django.db.models.deletion.CASCADE, to='curso.Categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellidos')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(help_text='El profesor del curso', on_delete=django.db.models.deletion.CASCADE, to='curso.Profesor'),
        ),
    ]
