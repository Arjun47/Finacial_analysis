from .models import Transaction
from rest_framework import viewsets, permissions
from .serializers import TranSerializer

class TranViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TranSerializer