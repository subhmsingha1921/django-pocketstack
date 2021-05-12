from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),

    path('auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),    
    path('auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    
    path('auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('questions/', include('questions.urls')),
    path('answers/', include('answers.urls')),
    path('auth/social/', include('social.urls')),
    
    path('redirect-to-app/', TemplateView.as_view(template_name='redirect_to_app.html')),
    path('password-reset-redirect/<slug:uidb64>/<slug:token>/', TemplateView.as_view(template_name='password_reset_redirect.html'), name='password_reset_redirect'),
]
