# Generated by Django 3.2.16 on 2023-01-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_libro_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
    ]