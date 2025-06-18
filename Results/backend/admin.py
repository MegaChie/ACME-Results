#!/usr/bin/env python3
"""
Dectates the admin control over the database.
"""
from django.contrib import admin
from .models import *


admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Year)
