#!/usr/bin/env python3
"""
Dictates the view logic for the table with the same name.
"""
from rest_framework import generics
from ..models.student import Student
from ..serializers.student_serializer import StudentSerializer



class StudentView(generics.ListCreateAPIView):
    """
    Controls HTTP GET and POST Requests.
    """
    queryset = Student.objects,all()
    serializer_class = StudentSerializer


class StudentDeleteView(generics.DestroyAPIView):
    """
    Controls HTTP DELETE Requests.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(generics.UpdateAPIView):
    """
    Controls HTTP PUT Requests.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
