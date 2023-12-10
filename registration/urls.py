
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path as url
from django.views.static import serve

from django.conf import settings


urlpatterns = [
    url(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('api/', include('registration_form.urls')),
    path('registrationPortalDatabase/defender', include('defender.urls')),
]