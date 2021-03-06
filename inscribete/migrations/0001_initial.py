# Generated by Django 2.1.7 on 2019-05-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscribete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=900)),
                ('apellido', models.CharField(max_length=900)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('fecha_de_nacimiento', models.DateTimeField()),
                ('lugar_de_nacimiento', models.CharField(max_length=900)),
                ('numero_de_telefono', models.IntegerField()),
                ('preparacion_academica', models.CharField(max_length=900)),
                ('direccion', models.CharField(max_length=900)),
                ('pueblo', models.CharField(max_length=900)),
                ('pais', models.CharField(max_length=900)),
                ('zip_code', models.IntegerField()),
                ('ocupacion', models.CharField(max_length=900)),
                ('telefono_del_trabajo', models.IntegerField()),
                ('lugar_del_trabajo', models.CharField(max_length=900)),
            ],
        ),
    ]
