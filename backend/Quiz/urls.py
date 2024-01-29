from django.urls import path, include
from .views import   available_exams, exam_detail,exam_quiz

urlpatterns = [

    path('available_exams/', available_exams, name='available_exams'),
    path('api/exam/<uuid:exam_id>/', exam_detail, name='exam-detail'),
    path('api/exam_quiz/<uuid:exam_id>/', exam_quiz, name='go_to_quiz'),
 
]
 
 

 