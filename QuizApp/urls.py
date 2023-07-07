from django.urls import path

from .views import ThemeFindView, BlogView

urlpatterns = [
    path('theme', BlogView.as_view(), name='theme'),
    path('post/theme', ThemeFindView.as_view(), name='post_theme')
]

