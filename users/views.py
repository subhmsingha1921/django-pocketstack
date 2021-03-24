from rest_framework import generics
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .models import CustomUser
from .serializers import CustomUserListSerializer, CustomUserDetailSerializer

# Create your views here.
class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name']


class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer