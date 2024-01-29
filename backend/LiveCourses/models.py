from django.db import models
from django.utils.text import slugify
from Users.models import CustomUser

class LiveCourse(models.Model):
    course_name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="files/images")
    title_description = models.TextField(null=True, blank=True)
    video_id = models.CharField(max_length=100)
    height = models.CharField(max_length=500)
    time = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    start = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='livecourse')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(LiveCourse, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    PAY = 'pay'
    WAITING = 'waiting'
    UNDONE = 'undone'
    CHOICES_STATUS = [
        (PAY, 'Pay'),
        (WAITING, 'Waiting'),
        (UNDONE, 'Undone'),
    ]

    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=WAITING)
    course = models.ForeignKey(LiveCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course.course_name}"
 