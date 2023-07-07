from django.db import models


# create model for quiz
class Quiz(models.Model):
    # foregn key to theme
    theme = models.ForeignKey('ThemeQuiz', on_delete=models.CASCADE)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    question = models.CharField(max_length=500)

    CHOISES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    answer = models.CharField(max_length=1, choices=CHOISES)


class ThemeQuiz(models.Model):
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.theme
