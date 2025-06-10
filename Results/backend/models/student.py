#!/usr/bin/env python3
"""
Dectates the model for the institues students.
"""
from django.db import models
from uuid import uuid4
from .faculty import Faculty
from .year import Year



class Student(models.Model):
    """
    Model for the students inlisted.
    """
    ID = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, blank=True, null=True)
    registeration_year = models.ForeignKey(Year, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        """
        Prints the student information.
        """
        intel =  [f"Student {self.name} studies at {self.faculty.name}:\n"]
        for attr, value in self.__dict__.items():
            intel.append(f"\t- {attr}: {value}\n")
        
        return "".join(intel)

