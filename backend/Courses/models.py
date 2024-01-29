from django.db import models
from uuid import uuid4
import uuid
from django.core.validators import MaxValueValidator,MinValueValidator

from Users.models import CustomUser
from Quiz.models import Exam, Question


 
class CategoryCourse(models.Model):
    title = models.CharField(max_length=255, verbose_name='CategoryCourse')
    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CategoryCourse , null = False , on_delete=models.CASCADE)
    intro_video = models.CharField(max_length = 100 , null = False)
    title=models.CharField(max_length=225)
    description = models.CharField(max_length = 200 , null = True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "files/thumbnail" ) 
    image_url=models.ImageField(upload_to='files/course_images') 
    resource = models.FileField(upload_to = "files/resource")
    length = models.IntegerField(null=False)
    # author = models.ManyToManyField(CustomUser, related_name='enrolled_courses')
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='course')
    course_uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    language=models.CharField(max_length=225)
    course_length=models.CharField(default=0,max_length=20)
    rating=models.ManyToManyField('Rate',blank=True)
    course_sections=models.ManyToManyField('CourseSection',blank=True)
    comment=models.ManyToManyField('Comment',blank=True)

    def __str__(self):
        return self.title



class UserCourse(models.Model):
    student = models.ManyToManyField(CustomUser, related_name='enrolled_courses')
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} - {self.course}'



class Rate(models.Model):
    rate_number=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

 

class CourseSection(models.Model):
    section_title=models.CharField(max_length=225, verbose_name='section Title',blank=True,null=True)
    description = models.TextField(verbose_name='Description',blank=True)
    section_number=models.IntegerField(blank=True,null=True)
    episodes=models.ManyToManyField('Episode',blank=True)

    def __str__(self):
        return self.section_title
    
class EpisodeQuiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Exam Title',blank=True)
    description = models.TextField(verbose_name='Description',blank=True)
    questions = models.ManyToManyField(Question, related_name='episodequiz',blank=True)
    def __str__(self):
        return self.title
 

class Episode(models.Model):
    episode_uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    title=models.CharField(max_length=225,blank=True)
    # file=CloudinaryField(resource_type='video',validators=[validate_video],folder='media')
    # file=models.FileField(upload_to='courses',validators=[validate_video],)
    length=models.DecimalField(max_digits=100,decimal_places=2,blank=True)
    video_id = models.CharField(max_length = 100 , null = False)
    is_preview = models.BooleanField(default = False)
    watched= models.BooleanField(default = False)
    exam = models.ForeignKey( EpisodeQuiz , on_delete=models.CASCADE,blank=True)
    serial_number = models.IntegerField(null=False)
 

    def __str__(self):
        return self.title
    

 
class Comment(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message=models.TextField()
    created=models.DateTimeField(auto_now=True)


class CouponCode(models.Model):
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    Code  = models.CharField(max_length = 100 , null = False)
    date = models.DateField( blank=True, null=True)
    time = models.TimeField( blank=True, null=True)
    def __str__(self):
        return self.Code
 
 
 