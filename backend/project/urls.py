# project/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Home.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('Courses/', include('Courses.urls')),
    path('LiveCourses/', include('LiveCourses.urls')),
    path('Quiz/', include('Quiz.urls')),
    path('Users/', include('Users.urls')),

   
 
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
