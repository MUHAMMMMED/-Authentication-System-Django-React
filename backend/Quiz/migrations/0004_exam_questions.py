# Generated by Django 5.0 on 2023-12-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(related_name='exams', to='Quiz.question'),
        ),
    ]
