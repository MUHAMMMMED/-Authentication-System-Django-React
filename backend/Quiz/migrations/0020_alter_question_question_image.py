# Generated by Django 5.0 on 2024-01-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0019_alter_question_correct_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='files/question_images/', verbose_name='Question Image'),
        ),
    ]