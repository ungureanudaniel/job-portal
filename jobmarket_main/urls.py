from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.contrib.auth import views as auth_views
from users.views import register, profile, contact, about, privacy, terms, pricing
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    ]
urlpatterns += i18n_patterns(
    path('users/', include('users.urls')),
    path('', include('candidates.urls')),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
