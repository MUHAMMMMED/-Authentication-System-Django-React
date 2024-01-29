from django.contrib import admin
from .models import QuestionCategory, Exam, UserExam, Question, ExamSubmission

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creator')
    # Add any other fields you want to display in the list

@admin.register(UserExam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'date',)
    filter_horizontal = ('student',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('question_content', 'category', 'correct_option',)
    # filter_horizontal = ('exams','correct_option', )
    pass

@admin.register(ExamSubmission)
class ExamSubmissionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'user', 'score', 'time_taking',)
    filter_horizontal = ('wrong_answers',)
