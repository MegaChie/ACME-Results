#!/usr/bin/env python3
"""
Handels the object-to-json and vise-versa convertion.
"""
from rest_framework import serializers
from ..models.subject import Subject



class SubjectSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        """
        Meta information for the serializer.
        """
        model = Subject
        fields = "__all__"
