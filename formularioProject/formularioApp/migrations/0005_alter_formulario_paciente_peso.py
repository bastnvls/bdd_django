# Generated by Django 4.2.5 on 2023-11-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioApp', '0004_delete_datos_paciente_delete_proyecto_intento1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario_paciente',
            name='peso',
            field=models.FloatField(),
        ),
    ]