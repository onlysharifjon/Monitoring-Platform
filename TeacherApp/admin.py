from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["full_name", "birth_date", "birth_place", "education_level", "specialty", "scientific_degree",
                    "scientific_title"]
    list_filter = ["education_level", "specialty", "scientific_degree", "scientific_title"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["subject", "teacher", "time", "week_day", "duration"]
    list_filter = ["subject", "teacher", "time", "week_day", "duration"]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register([
    EduLevel, Specialty, ScientificDegree, ScientificTitle,
    ForeignLangs, Subject, Room, Group
])
