# Generated by Django 5.0.1 on 2024-04-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='instagra_id',
            new_name='instagrm_id',
        ),
    ]
