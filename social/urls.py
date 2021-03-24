from django.urls import path
from .views import FacebookLogin, GoogleLogin


urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
]
