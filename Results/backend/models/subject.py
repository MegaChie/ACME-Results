#!/usr/bin/env python3
"""
Dectates the model for the institue subjcts.
"""
from django.db import models
from uuid import uuid4
from .semester import Semester



class Subject(models.Model):
    """
    Model for the subjects taught in the institute.
    """
    name = models.CharField(max_length=128, blank=True, null=True)
    ID = models.UUIDField(primary_key=True, default=uuid4)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        """
        Prints the name of the subject.
        """
        return self.name
    
    class Meta:
        """
        Sets the meta information for the model.
        """
        indexes = [
            models.Index(fields=["ID"])
            ]
