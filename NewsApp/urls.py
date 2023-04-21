# urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogViewSet

blog_list = BlogViewSet.as_view({'get': 'list'})


urlpatterns = [
    path('blogs/v1', blog_list, name='blog-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
