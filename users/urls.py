from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import user_login, register, contact, about, account, privacy, terms, registration_conf_view, registration_success_view, maintenance


urlpatterns = [
    path('login/', user_login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('register/registration_confirmation/', registration_conf_view, name='registration_confirmation'),
    path('register/registration_success/', registration_success_view, name='registration_success'),
    # path('review/', include('review.urls')),
    path('account/', account, name='account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('terms-of-service/', terms, name='terms-of-service'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
