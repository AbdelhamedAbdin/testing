# Generated by Django 3.1.1 on 2021-05-23 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_grade', '0003_auto_20210523_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_grade.character'),
        ),
    ]
