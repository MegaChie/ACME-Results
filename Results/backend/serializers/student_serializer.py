#!/usr/bin/env python3
"""
Handels the object-to-json and vise-versa convertion.
"""
from rest_framework import serializers
from ..models.student import Student



class StudentSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        """
        Meta information for the serializer.
        """
        model = Student
        fields = "__all__"
