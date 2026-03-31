from django.contrib import admin

from home.models import Student

# Register your models here.
from .models import *

admin.site.register(Receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=["student", 'subject', "marks"]

admin.site.register(SubjectMarks, SubjectMarksAdmin)