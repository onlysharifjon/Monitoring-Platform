# Generated by Django 4.2 on 2023-07-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='themequiz',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QuizApp.themequiz'),
            preserve_default=False,
        ),
    ]
