#!/usr/bin/env python3
"""
Handels the object-to-json and vise-versa convertion.
"""
from rest_framework import serializers
from ..models.semester import Semester



class SemesterSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        """
        Meta information for the serializer.
        """
        model = Semester
        fields = "__all__"
