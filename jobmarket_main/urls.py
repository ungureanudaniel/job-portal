from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.contrib.auth import views as auth_views
from users.views import register, account, user_login, contact, about, privacy, terms, pricing
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('hiring/', include('recruiters.urls')),
    path('', include('candidates.urls')),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    # path('', include('pwa.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
