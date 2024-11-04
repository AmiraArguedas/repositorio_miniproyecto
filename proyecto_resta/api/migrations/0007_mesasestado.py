# Generated by Django 5.1.2 on 2024-11-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_metododepago'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesasEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_mesa_creado', models.DateTimeField(auto_now_add=True)),
                ('estado_mesa_actualizado', models.DateTimeField(auto_now=True)),
                ('nombre_estado', models.CharField(choices=[('disponible', 'Disponible'), ('reservada', 'Reservada'), ('Disponible', 'disponible'), ('Reservada', 'reservada')], max_length=50)),
            ],
        ),
    ]
