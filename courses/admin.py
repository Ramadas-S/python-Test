from django.contrib import admin
from . models import Course

# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


admin.site.register(Course)