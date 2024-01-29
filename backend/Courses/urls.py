 
from django.urls import path
from .views import CourseListView, CourseDetailView, EpisodeDetailView,NextEpisode

urlpatterns = [
    path('api/', CourseListView.as_view(), name='course-list'),
    # path('api/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('api/<uuid:course_uuid>/', CourseDetailView.as_view(), name='course-detail'),

    path('api/episode/<uuid:episode_uuid>/', EpisodeDetailView.as_view(), name='episode-detail'),
    # path('api/<int:serial_number>/', EpisodeDetailView.as_view(), name='episode-detail')
 
    path('api/next-episode/<uuid:episode_uuid>/', NextEpisode.as_view(), name='next-episode'),
 
 ]
 