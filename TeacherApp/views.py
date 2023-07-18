from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Teacher
from .serializers import TeacherSerializer


class SingleTeacherView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class AllTeachersView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
