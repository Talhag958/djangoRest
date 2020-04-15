from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie,Ratings
from rest_framework import permissions
from .serializers import MovieSerializer,RatingSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
        