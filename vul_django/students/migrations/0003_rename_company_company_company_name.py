# Generated by Django 4.0.8 on 2023-05-09 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_company_alter_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company',
            new_name='company_name',
        ),
    ]
