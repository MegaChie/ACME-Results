#!/usr/bin/env python3
"""
Dectates the model for the institues faculties.
"""
from django.db import models
from uuid import uuid4



class Faculty(models.Model):
    """
    Model for the different faculties.
    """
    ID = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        """
        Prints the discription of the faculty.
        """
        return f"{self.name}: {self.description}"
    
    class Meta:
        """
        Sets the meta information for the model.
        """
        indexes = [
            models.Index(fields=["name"])
            ]

