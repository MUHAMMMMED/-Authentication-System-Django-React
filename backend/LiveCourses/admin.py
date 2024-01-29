from django.contrib import admin
from .models import LiveCourse, Enrollment

@admin.register(LiveCourse)
class LiveCourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'active', 'price', 'date', 'start')
    search_fields = ('course_name',)
    prepopulated_fields = {'slug': ('course_name',)}

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'status', 'created_at')
    search_fields = ('name', 'email', 'course__course_name')
