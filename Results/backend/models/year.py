#!/usr/bin/env python3
"""
Dectates the model for the year of registration.
"""
# Might be added later as part of the student Model.
from django.db import models


class Year(models.Model):
    """
    Model for the study year.
    """
    start_year = models.PositiveBigIntegerField(null=False)
    end_year = models.IntegerField(blank=True) 

    def __str__(self) -> str:
        """
        Prints the discription of the registeration year.
        """
        return f"Registeration year of {self.start_year} - {self.end_year}"
    
    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically compute end_year.
        """
        if self.start_year is not None:
            self.end_year = self.start_year + 1
        super().save(*args, **kwargs)

    
    class Meta:
        """
        Sets the meta information for the model.
        """
        pass # For now.
