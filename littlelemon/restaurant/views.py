from django.shortcuts import render
from .serializers import MenuSerializer, BookingTableSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import MenuTable, BookingTable
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes



def index(req):
    return render(req, 'index.html', {})

@permission_classes([IsAdminUser])
class MenuView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    permission_classes = [IsAuthenticated]

@permission_classes([AllowAny])
class MenuItems(generics.ListAPIView,):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer





