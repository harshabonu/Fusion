# Generated by Django 3.1.5 on 2024-04-20 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0001_initial'),
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authentication',
            name='course',
        ),
        migrations.AddField(
            model_name='authentication',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academic_information.course'),
        ),
        migrations.AddField(
            model_name='authentication',
            name='course_year',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='grade',
            name='semester_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]