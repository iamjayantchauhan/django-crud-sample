# user_data/views.py
from rest_framework import viewsets
from .models import UserData
from .serializers import UserDataSerializer


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Customize queryset if needed, for example, filter by the current user
        return queryset

    def perform_update(self, serializer):
        serializer.save()