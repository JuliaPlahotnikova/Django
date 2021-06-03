# Generated by Django 3.1 on 2021-04-18 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('logo', models.ImageField(blank=True, default='company.png', null=True, upload_to='')),
                ('location', models.CharField(max_length=32, null=True)),
                ('description', models.CharField(max_length=32, null=True)),
                ('employee_count', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('title', models.CharField(db_index=True, max_length=32)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=124)),
                ('skills', models.CharField(db_index=True, max_length=124)),
                ('description', models.TextField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('token', models.TextField(default='')),
                ('profile_pic', models.ImageField(blank=True, default='check.png', null=True, upload_to='')),
                ('first_name', models.CharField(max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=32, null=True)),
                ('education', models.CharField(max_length=500, null=True)),
                ('experience', models.CharField(max_length=32, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('portfolio', models.CharField(max_length=32, null=True)),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.grademodel')),
                ('specialty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.specialty')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='vacancies.statusmodel')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=32)),
                ('written_phone', models.CharField(max_length=32)),
                ('written_cover_letter', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancies.vacancy')),
            ],
        ),
    ]