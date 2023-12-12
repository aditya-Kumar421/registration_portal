from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('registration_form.urls')),
    path('admin/defender', include('defender.urls')),
]