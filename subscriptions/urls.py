from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import delete_subscribers_view, subscription_confirmation_view

urlpatterns = [
    path('unsubscribe/', delete_subscribers_view, name='unsubscribe'),
    path('subscription/subscription_confirmation/', subscription_confirmation_view, name='subscription_confirmation'),
    path('subscription_confirmation/', subscription_confirmation_view, name='subscription_confirmation'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
