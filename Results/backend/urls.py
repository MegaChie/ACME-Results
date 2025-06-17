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
    path("del_faculties", FacultyDeleteView.as_view(),
         name="Delete Faculty"),
    path("edit_faculies", FacultyUpdateView.as_view(),
         name="Edit Faculty"),

    # Semester related
    path("semesters", SemesterView.as_view(),
         name="Semester List"),
    path("del_semester", SemesterDeleteView.as_view(),
         name="Delete Semester"),
    path("edit_semesters", SemesterUpdateView.as_view(),
         name="Update Semester"),

    # Student related
    path("students", StudentView.as_view(),
         name="Student List"),
    path("del_students", StudentDeleteView.as_view(),
         name="Delete Student"),
    path("edit_students", StudentUpdateView.as_view(),
         name="Edit Student"),

    # Subject related
    path("subjects", SubjectView.as_view(),
         name="List Subjects"),
    path("del_subjects", SubjectDeleteView.as_view(),
         name="Delete Subject"),
    path("edit_subject", SubjecUpdateView.as_view(),
    name="Edit Subject"),

    # Year related
    path("years", YearView.as_view(),
         name="Year List"),
    path("del_years", YearDeleteView.as_view(),
         name="Delete Year"),
    path("edit_years", YearUpdateView.as_view(),
         name="Edit Year")
]
