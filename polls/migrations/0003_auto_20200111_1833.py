# Generated by Django 3.0.2 on 2020-01-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200111_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='polls/static/polls/img/'),
        ),
    ]
