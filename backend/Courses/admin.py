 

from django.contrib import admin
from .models import CategoryCourse, Course, Rate, CourseSection, EpisodeQuiz, Episode, Comment, CouponCode,UserCourse

@admin.register(CategoryCourse)
class CategoryCourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    pass

@admin.register(EpisodeQuiz)
class ExamVideoAdmin(admin.ModelAdmin):
    pass

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(CouponCode)
class CouponCodeAdmin(admin.ModelAdmin):
    pass

@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    pass
