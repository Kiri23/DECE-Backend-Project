# Generated by Django 2.1.7 on 2019-05-04 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inscribete', '0004_auto_20190504_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='registracion',
            name='estudiante',
            field=models.ForeignKey(default=None, help_text='El estudiante que se esta registrando', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registracion',
            name='curso',
            field=models.ForeignKey(help_text='El curso que el estudiante se esta registrando', on_delete=django.db.models.deletion.CASCADE, to='curso.Curso'),
        ),
    ]