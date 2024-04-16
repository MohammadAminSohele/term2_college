from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "mobile",
        "first_name",
        "last_name",
        "nat_code",
    )
    search_fields = (
        "first_name",
        "last_name",
        "mobile",
    )
    ordering = (
        "last_name",
        "first_name",
    )
    list_per_page = 25


@admin.register(models.DegreeOfEducation)
class DegreeOfEducationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "study",
    )
    search_fields = (
        "name",
        "study",
    )
    list_per_page = 25


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "mobile",
        "first_name",
        "last_name",
        "nat_code",
    )
    search_fields = (
        "first_name",
        "last_name",
        "mobile",
        "email",
    )
    ordering = (
        "last_name",
        "first_name",
    )
    list_per_page = 25


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "regdate",
    )
    search_fields = ("name",)
    list_per_page = 25


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "regdate",
    )
    search_fields = (
        "name",
        "level__name",
    )
    list_per_page = 25


@admin.register(models.Term)
class TermAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "regdate",
    )
    list_per_page = 20


@admin.register(models.StudentTerm)
class StudentTermAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "course",
        "term",
        "regdate",
    )
    list_per_page = 25
