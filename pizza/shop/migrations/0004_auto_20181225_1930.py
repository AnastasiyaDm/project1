# Generated by Django 2.1.4 on 2018-12-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181225_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.CharField(choices=[('cheese', 'Quattro Formaggi'), ('chicken', 'Quattro Stagioni'), ('mushroom', 'Funghi'), ('seafood', 'Frutti di Mare'), ('assorti', 'Assorti'), ('fruits', 'Fruits'), ('beef', 'Boscaiola'), ('hawaii', 'Hawaii'), ('green', 'Braccio di Ferro'), ('mozarella', 'Crudo'), ('vegetables', 'Vegetariana'), ('sausages', 'Bavaria')], default='cheese', max_length=15, verbose_name='Пицца'),
        ),
    ]