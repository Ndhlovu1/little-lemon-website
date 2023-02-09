from django.shortcuts import render
from .serializers import MenuSerializer, BookingTableSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import MenuTable, BookingTable
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


def index(req):
    return render(req, 'index.html', {})

class MenuView(generics.ListCreateAPIView):

    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    permission_classes = [IsAuthenticated]







