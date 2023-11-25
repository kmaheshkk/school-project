# Generated by Django 4.2.7 on 2023-11-19 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_course_department_person_delete_commerce_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='country',
            new_name='department',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolapp.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolapp.department'),
        ),
    ]
