from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register, user_login, user_logout, contact, about,\
 profile, dashboard, privacy, terms, registration_conf_view,\
 registration_success_view, add_service_view

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('register2/', register, name='register2'),
    path('register/registration_confirmation/', registration_conf_view, name='registration_confirmation'),
    path('register/registration_success/', registration_success_view, name='registration_success'),
    # path('review/', include('review.urls')),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_service/', add_service_view, name='add_service'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('terms-of-service/', terms, name='terms-of-service'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
