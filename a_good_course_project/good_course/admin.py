from django.contrib import admin
from good_course.models import School, Course, UserProfile

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'school', 'description']

class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'tag':('name',)}

admin.site.register(School, SchoolAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfile)
