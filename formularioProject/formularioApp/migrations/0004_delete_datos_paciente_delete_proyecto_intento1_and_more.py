# Generated by Django 4.2.5 on 2023-11-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioApp', '0003_formulario_paciente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Datos_Paciente',
        ),
        migrations.DeleteModel(
            name='Proyecto_intento1',
        ),
        migrations.AlterField(
            model_name='formulario_paciente',
            name='peso',
            field=models.IntegerField(),
        ),
    ]
