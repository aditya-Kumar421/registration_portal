from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('registrationPortalDatabase/', admin.site.urls),
    path('api/', include('registration_form.urls')),
    path('registrationPortalDatabase/defender', include('defender.urls')),
]