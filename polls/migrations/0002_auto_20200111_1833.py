# Generated by Django 3.0.2 on 2020-01-11 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imgae',
            new_name='image',
        ),
    ]