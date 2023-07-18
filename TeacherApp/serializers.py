from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    scientific_title = serializers.SlugField('title')
    scientific_degree = serializers.SlugField('title')
    education_level = serializers.SlugField('title')
    specialty = serializers.SlugField('title')
    foreign_langs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Teacher
        fields = "__all__"
