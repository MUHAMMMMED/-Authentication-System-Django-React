# Generated by Django 5.0 on 2023-12-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_exam_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_new_exam', models.BooleanField(default=False)),
            ],
        ),
    ]
