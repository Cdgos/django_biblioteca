# Generated by Django 3.2.16 on 2023-01-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0008_libro_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]