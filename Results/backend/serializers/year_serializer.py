#!/usr/bin/env python3
"""
Handels the object-to-json and vise-versa convertion.
"""
from rest_framework import serializers
from ..models.year import Year



class YearSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        """
        Meta information for the serializer.
        """
        model = Year
        fields = "__all__"
