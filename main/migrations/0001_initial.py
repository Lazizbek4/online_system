# Generated by Django 3.1.1 on 2021-06-23 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('attendance', models.CharField(choices=[('X', 'X'), ('O', 'O')], default='X', max_length=8)),
            ],
            options={
                'verbose_name': 'Attendance Weeks',
                'verbose_name_plural': 'Attendance Weeks',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'All Classes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('message', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Submission')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date Modification')),
            ],
            options={
                'verbose_name': 'Contact Request',
                'verbose_name_plural': 'Contact Requests',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_num', models.CharField(default='Unknown', max_length=32)),
            ],
            options={
                'verbose_name': 'Groups',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'Lesson Type',
                'verbose_name_plural': 'Lesson Types',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('class_name', models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to='main.class')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.groups')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'All Students',
            },
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.attendance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name': 'Student Attendance',
                'verbose_name_plural': 'Student Attendance',
            },
        ),
    ]
