from django.urls import path, include
from django.conf import settings
from .views import home, job_search_list

urlpatterns = [
    path('', home, name="home"),
    path('job/', job_search_list, name='job-search-list'),
]
