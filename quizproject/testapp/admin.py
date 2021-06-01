from django.contrib import admin
from testapp.models import Course, Question
# Register your models here.

class AdminQuestion(admin.ModelAdmin):
    list_display=['course','question','answer']
class AdminCourse(admin.ModelAdmin):
    list_display=['course_name']

    


admin.site.register(Course,AdminCourse)
admin.site.register(Question,AdminQuestion)
