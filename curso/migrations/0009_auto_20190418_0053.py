# Generated by Django 2.1.7 on 2019-04-18 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0008_auto_20190418_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='temas',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='curso.Curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='temas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prontuario', to='curso.Temas'),
        ),
    ]
