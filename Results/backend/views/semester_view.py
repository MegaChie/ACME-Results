#!/usr/bin/env python3
"""
Dictates the view logic for the table with the same name.
"""
from rest_framework import generics
from ..models.semester import Semester
from ..serializers.semester_serializer import SemesterSerializer



class SemesterView(generics.ListCreateAPIView):
    """
    Controls HTTP GET and POST Requests.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDeleteView(generics.DestroyAPIView):
    """
    Controls HTTP DELETE Requests.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterUpdateView(generics.UpdateAPIView):
    """
    Controls HTTP PUT Requests.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
