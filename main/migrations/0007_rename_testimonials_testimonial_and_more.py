# Generated by Django 4.1.4 on 2024-01-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_offers_offer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
    ]