from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
# Create your views here.


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()