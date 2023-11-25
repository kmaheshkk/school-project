# Generated by Django 4.2.7 on 2023-11-23 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_alter_student_course_alter_student_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='department',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolapp.course'),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolapp.department'),
        ),
    ]
