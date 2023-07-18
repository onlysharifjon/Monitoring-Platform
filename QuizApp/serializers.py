from rest_framework import serializers

from .models import ThemeQuiz, Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeQuiz
        fields = ('theme',)


class QuizFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('theme', 'question', 'A', 'B', 'C', 'D', 'answer')
