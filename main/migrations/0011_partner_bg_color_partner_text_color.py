# Generated by Django 4.1.4 on 2024-01-13 13:47

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_page_hero_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='bg_color',
            field=colorfield.fields.ColorField(default='rgb(243, 243, 243)', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='partner',
            name='text_color',
            field=colorfield.fields.ColorField(default='rgb(38, 134, 146)', image_field=None, max_length=18, samples=None),
        ),
    ]