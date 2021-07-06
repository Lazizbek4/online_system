# Generated by Django 3.1.1 on 2021-06-27 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210626_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('scheduled_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.schedulelesson')),
                ('students', models.ManyToManyField(to='main.Student')),
            ],
            options={
                'verbose_name': 'Group Attendance',
                'verbose_name_plural': 'Group Attendance',
            },
        ),
    ]