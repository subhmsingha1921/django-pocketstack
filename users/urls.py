from django.urls import path

from .views import CustomUserListView, CustomUserDetailView


urlpatterns = [
    path('', CustomUserListView.as_view(), name='user_list'),
    path('<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
]
