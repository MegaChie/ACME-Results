#!/usr/bin/env python3
"""
Dictates the view logic for the table with the same name.
"""
from rest_framework import generics
from ..models.year import Year
from ..serializers.year_serializer import YearSerializer



class YearView(generics.ListCreateAPIView):
    """
    Controls HTTP GET and POST Requests.
    """
    queryset = Year.objects.all()
    serializer_class = YearSerializer
