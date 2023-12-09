from django.urls import path
from .views import RegistrationList#, captchaView


urlpatterns = [
    path('registration/', RegistrationList.as_view(), name='registration'),
    # path('captcha/', captchaView.as_view(), name='cpatcha'),
]
