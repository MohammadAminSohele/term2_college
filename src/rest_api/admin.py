from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = get_user_model().objects.filter(is_staff=False, is_superuser=False, is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_first_name(self, obj):
        return obj.user.first_name

    get_first_name.short_description = _('first name')

    def get_last_name(self, obj):
        return obj.user.last_name
    
    get_last_name.short_description = _('last name')

    list_display = (
        "mobile",
        "get_first_name",
        "get_last_name",
        "nat_code",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "mobile",
    )
    ordering = (
        "user__last_name",
        "user__first_name",
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

    def get_first_name(self, obj):
        return obj.user.first_name

    get_first_name.short_description = _('first name')

    def get_last_name(self, obj):
        return obj.user.last_name
    
    get_last_name.short_description = _('last name')


    list_display = (
        "mobile",
        "get_last_name",
        "get_first_name",
        "nat_code",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "mobile",
        "user__email",
    )
    ordering = (
        "user__last_name",
        "user__first_name",
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
