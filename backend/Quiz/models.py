 
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from Users.models import CustomUser

class QuestionCategory(models.Model):
  name = models.CharField(max_length=255, verbose_name='Category Name')

  def __str__(self):
    return self.name

class Exam(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  title = models.CharField(max_length=255, verbose_name='Exam Title')
  description = models.TextField(verbose_name='Description')
  creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_exams')
  time_to_answer = models.IntegerField(default=60, verbose_name='Time to Answer ')

  def __str__(self):
    return self.title
 
class UserExam(models.Model):
    student = models.ManyToManyField(CustomUser, related_name='enrolled_exam')
    exam = models.ForeignKey(Exam , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tries = models.FloatField(default=1, verbose_name='tries')
    # def __str__(self):
    #     return f'{self.student} - {self.exam}'
   








class Question(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  exams = models.ManyToManyField(Exam, related_name='questions')
  category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name='questions')
  question_content = models.TextField(verbose_name='Question Content', null=True, blank=True, )
  question_image = models.ImageField(upload_to='files/question_images/', null=True, blank=True, verbose_name='Question Image')
  question_video_youtube = models.CharField(max_length = 100 ,null=True, blank=True)
  question_video = models.FileField(upload_to='question_videos/', null=True, blank=True, verbose_name='Question Video')
  option_A = models.CharField(max_length=500)
  option_B = models.CharField(max_length=500)
  option_C = models.CharField(max_length=500, blank=True)
  option_D = models.CharField(max_length=500, blank=True)
  # time_to_answer = models.IntegerField(default=60, verbose_name='Time to Answer (in seconds)')
  # marks = models.IntegerField(default=5)
  correct_option = models.CharField(max_length=1, choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')])
  def __str__(self):
     return f'{self.question_content} - {self.correct_option}'
  


 



  

class ExamSubmission(models.Model):
  exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='submissions')
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='exam_submissions')
  score = models.FloatField(default=0, verbose_name='Exam Score')
  time_taking= models.IntegerField(default=0,)
  wrong_answers = models.ManyToManyField(Question, blank=True)

 















