from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/bark-bark/', views.project_bark_bark, name='project_bark_bark'),
    path('project/utopia/', views.project_utopia, name='project_utopia'),
    path('project/teencon/', views.project_teencon, name='project_teencon'),
]
