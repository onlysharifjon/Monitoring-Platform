from django.shortcuts import render

# Create your views here.

from .models import ThemeQuiz, Quiz
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuizSerializer, QuizFindSerializer
from drf_yasg.utils import swagger_auto_schema


class BlogView(APIView):
    # @swagger_auto_schema(request_body=BlogSerializer)
    def get(self, request):
        # blog objects send all
        blogs = ThemeQuiz.objects.all()
        serializer = QuizSerializer(blogs, many=True)
        return Response(serializer.data)


# class ThemeFindView(APIView):
#     @swagger_auto_schema(request_body=QuizSerializer)
#     def post(self, request):
#         # blog objects send all
#         theme = ThemeQuiz.objects.filter(theme=request.data['theme'])
#         print(theme)
#         blogs = Quiz.objects.filter(theme=theme).all()
#         print(blogs)
#         serializer = QuizSerializer(blogs, many=True)
#         return Response(serializer.data)

class ThemeFindView(APIView):
    @swagger_auto_schema(request_body=QuizSerializer)
    def post(self, request):
        theme = request.data.get('theme')
        obj = Quiz.objects.filter(theme__theme=theme)
        serializer = QuizFindSerializer(obj, many=True)
        return Response(serializer.data)
