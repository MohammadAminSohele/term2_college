# Generated by Django 5.0.4 on 2024-05-10 13:19

import django.core.validators
import django.db.models.deletion
import rest_api.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeOfEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Name of degree')),
                ('study', models.TextField(max_length=200, verbose_name='Field of Study')),
            ],
            options={
                'verbose_name': 'DegreeOfEducation',
                'verbose_name_plural': 'DegreeOfEducations',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Section name')),
                ('regdate', models.DateField(null=True, verbose_name='Date of Registration')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
                'ordering': ['regdate'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Term name')),
                ('startDate', models.DateField(verbose_name='Start date')),
                ('endDate', models.DateField(verbose_name='End date')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Term',
                'verbose_name_plural': 'Terms',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nat_code', models.CharField(max_length=10, unique=True, verbose_name="Student's national code")),
                ('birthday_date', models.DateField(verbose_name='Date of birth')),
                ('telephone', models.CharField(max_length=11, verbose_name='landline number')),
                ('mobile', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number.', regex='^09\\d{2}\\s*?\\d{3}\\s*?\\d{4}$')], verbose_name='Phone number')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('description', models.TextField(verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'ordering': ['user__first_name', 'regdate'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nat_code', models.CharField(max_length=10, unique=True, verbose_name="Teacher's national code")),
                ('birthday_date', models.DateField(verbose_name='Date of birth')),
                ('telephone', models.CharField(max_length=11, verbose_name='landline number')),
                ('mobile', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number.', regex='^09\\d{2}\\s*?\\d{3}\\s*?\\d{4}$')], verbose_name='Phone number')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('description', models.TextField(verbose_name='Description')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.degreeofeducation', verbose_name='Degree Of Education')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name of Course')),
                ('unit', models.PositiveSmallIntegerField(default=1, verbose_name='unit')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('description', models.TextField(verbose_name='Description')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.level', verbose_name='Section')),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='rest_api.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['level'],
            },
        ),
        migrations.CreateModel(
            name='StudentTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(blank=True, default=0, validators=[rest_api.models.validate_grade], verbose_name='student grade')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('endDate', models.DateTimeField(verbose_name='End date')),
                ('description', models.TextField(verbose_name='Description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.course', verbose_name='Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.student', verbose_name='Student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.term', verbose_name='Term')),
            ],
            options={
                'verbose_name': 'Student Term',
                'verbose_name_plural': 'Student Terms',
            },
        ),
    ]
