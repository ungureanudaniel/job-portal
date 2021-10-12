from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('users.urls')),
    path('hiring/', include('recruiters.urls')),
    path('/', include('candidates.urls')),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('pwa.urls')),
]
