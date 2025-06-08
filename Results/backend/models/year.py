#!/usr/bin/env python3
"""
Dectates the model for the year of study.
"""
from django.db import models


class Year(models.Model):
    """
    Model for the study year.
    """
    start_year = models.PositiveBigIntegerField(null=False)
    end_year = models.IntegerField() # Function goes here

    def __str__(self) -> str:
        return f"Study year of {self.start_year} - {self.end_year}"
    
    def compute_end_year(self) -> None:
        """
        Calculates the end year based on the start year.
        """
        self.end_year = self.start_year + 1
        self.save()
        return
    
    class Meta:
        """
        Sets the meta information for the model.
        """
        pass # For now.
