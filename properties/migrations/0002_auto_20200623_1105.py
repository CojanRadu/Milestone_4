# Generated by Django 3.0.5 on 2020-06-23 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Features',
            new_name='Feature',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='image',
            new_name='image_name',
        ),
    ]