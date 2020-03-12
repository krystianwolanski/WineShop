# Generated by Django 3.0.2 on 2020-01-11 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20200111_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(choices=[('ARG', 'Argentyna'), ('AUS', 'Australia'), ('AUT', 'Austria')], default='AUS', max_length=10),
            preserve_default=False,
        ),
    ]
