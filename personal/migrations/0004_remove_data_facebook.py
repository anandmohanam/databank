# Generated by Django 5.0.1 on 2024-04-13 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_rename_facebook_id_data_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='facebook',
        ),
    ]
