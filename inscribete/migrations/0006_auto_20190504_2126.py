# Generated by Django 2.1.7 on 2019-05-04 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscribete', '0005_auto_20190504_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registracion',
            name='curso',
            field=models.ForeignKey(default=None, help_text='El curso que el estudiante se esta registrando', on_delete=django.db.models.deletion.CASCADE, to='curso.Curso'),
        ),
    ]
