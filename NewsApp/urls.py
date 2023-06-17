# urls.py
from django.urls import path
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogViewSet
from drf_yasg.views import get_schema_view
blog_list = BlogViewSet.as_view({'get': 'list'})



urlpatterns = [
    path('blogs/v1', blog_list, name='index'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
