# Generated by Django 4.2.7 on 2023-11-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_pedido_metodo_pedido_status_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Foto',
            field=models.CharField(max_length=100),
        ),
    ]
