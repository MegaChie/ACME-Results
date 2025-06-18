#!/usr/bin/env python3
"""
Dectates the urls behaviour.
"""
from django.urls import path
from .views import *



urlpatterns = [
    # Faculty related
    path("faculties", FacultyView.as_view(),
         name="Faculties List"),

    # Semester related
    path("semesters", SemesterView.as_view(),
         name="Semester List"),

    # Student related
    path("students", StudentView.as_view(),
         name="Student List"),

    # Subject related
    path("subjects", SubjectView.as_view(),
         name="List Subjects"),

    # Year related
    path("years", YearView.as_view(),
         name="Year List"),
]
