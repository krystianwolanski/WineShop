# Generated by Django 3.0.2 on 2020-01-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_product_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.CharField(choices=[('Argentyna', 'Argentyna'), ('Australia', 'Australia'), ('Austria', 'Austria')], max_length=10),
        ),
    ]
