# Generated by Django 2.1.7 on 2019-05-04 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscribete', '0003_registracion_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registracion',
            name='curso',
            field=models.ForeignKey(default=None, help_text='El profesor del curso', on_delete=django.db.models.deletion.CASCADE, to='curso.Curso'),
        ),
    ]
