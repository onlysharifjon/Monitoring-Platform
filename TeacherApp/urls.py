from django.urls import path, path
from .views import AllTeachersView, SingleTeacherView

urlpatterns = [
    path('all/', AllTeachersView.as_view(), name='all_blogs'),
    path('teacher/<int:pk>/', SingleTeacherView.as_view(), name='single_blog'),
]
