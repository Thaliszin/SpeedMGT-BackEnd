# Generated by Django 4.2.7 on 2023-11-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_pedido_preco_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_itens',
            name='precoXquantidade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
