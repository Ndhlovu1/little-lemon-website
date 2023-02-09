from django.shortcuts import render
from .serializers import MenuSerializer, BookingTableSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import MenuTable, BookingTable


def index(req):
    return render(req, 'index.html', {})

class MenuView(generics.ListCreateAPIView):

    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer







