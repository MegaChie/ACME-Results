#!/usr/bin/env python3
"""
Dectates the model for the study semester.
"""
from django.db import models
from uuid import uuid4



class Semester(models.Model):
    """
    Model representing a study semester.
    """
    semester_choices = [
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (5, "5th"),
        (6, "6th"),
        (7, "7th"),
        (8, "8th"),
        (9, "9th"),
        (10, "10th")
    ]
    number = models.IntegerField(null=False, unique=True,
                                 choices=semester_choices)
    ID = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    def __str__(self):
        """
        Prints the semester number.
        """
        return f"the {self.number} semester"

    class Meta:
        """
        Sets the meta information for the model.
        """
        indexes = [
            models.Index(fields=["ID"])
            ]
