#!/usr/bin/env python3
"""
Dictates the view logic for the table with the same name.
"""
from rest_framework import generics
from ..models.subject import Subject
from ..serializers.subject_serializer import SubjectSerializer



class SubjectView(generics.ListCreateAPIView):
    """
    Controls HTTP GET and POST Requests.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
