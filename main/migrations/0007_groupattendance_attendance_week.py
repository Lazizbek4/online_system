# Generated by Django 3.1.1 on 2021-06-27 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_groupattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupattendance',
            name='attendance_week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.attendance'),
        ),
    ]
