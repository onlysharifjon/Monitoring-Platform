# Generated by Django 4.2 on 2023-07-07 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(max_length=100)),
                ('B', models.CharField(max_length=100)),
                ('C', models.CharField(max_length=100)),
                ('D', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='QuizApp.quiz')),
            ],
        ),
    ]
