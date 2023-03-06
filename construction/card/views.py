from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

class CardViewset(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Card.objects.all()
    serializer_class = CardSerializer




