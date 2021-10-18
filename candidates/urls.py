from django.urls import path, include
from django.conf import settings
from .views import home, job_search_list, category, job_details

urlpatterns = [
    path('', home, name="home"),
    path('job/', job_search_list, name='job-search-list'),
    path('category/<slug:cat_slug>/', category, name='category'),
    path('job_details/<int:pk>', job_details, name='job_details'),
]
