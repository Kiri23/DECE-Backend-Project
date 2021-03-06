# Generated by Django 2.1.7 on 2019-04-18 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0009_auto_20190418_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='temas',
        ),
        migrations.RemoveField(
            model_name='temas',
            name='subtemas',
        ),
        migrations.AddField(
            model_name='subtemas',
            name='tema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Temas'),
        ),
        migrations.AlterField(
            model_name='temas',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Curso'),
        ),
    ]
