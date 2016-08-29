from django.shortcuts import render
from main.models import Casino
from main.serializers import CasinoSerializer
from rest_framework import generics


class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
