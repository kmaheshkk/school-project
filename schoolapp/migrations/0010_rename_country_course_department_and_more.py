# Generated by Django 4.2.7 on 2023-11-25 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_rename_course_person_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='country',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='city',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='country',
            new_name='department',
        ),
    ]
