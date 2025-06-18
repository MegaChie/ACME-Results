#!/usr/bin/env python3
"""
Dictates the view logic for the table with the same name.
"""
from rest_framework import generics
from ..models.faculty import Faculty
from ..serializers.faculty_serializer import FacultySerializer



class FacultyView(generics.ListCreateAPIView):
    """
    Controls HTTP GET and POST Requests.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
