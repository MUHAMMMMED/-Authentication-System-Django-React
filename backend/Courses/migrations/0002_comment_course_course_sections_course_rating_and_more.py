# Generated by Django 5.0 on 2024-01-14 23:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_sections',
            field=models.ManyToManyField(blank=True, to='Courses.coursesection'),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.ManyToManyField(blank=True, to='Courses.rate'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='episodes',
            field=models.ManyToManyField(blank=True, to='Courses.episode'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.AddField(
            model_name='course',
            name='comment',
            field=models.ManyToManyField(blank=True, to='Courses.comment'),
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
