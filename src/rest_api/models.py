from django.utils.translation import gettext as _
from django.db import models

# Create your models here.


class Student(models.Model):
    nat_code = models.CharField(
        max_length=150, verbose_name=_("Student's national code")
    )
    first_name = models.CharField(max_length=150, verbose_name=_("ّStudent's name"))
    last_name = models.CharField(max_length=150, verbose_name=_("Student's last name"))
    birthday_date = models.DateField(verbose_name=_("Date of birth"))
    telephone = models.CharField(max_length=150, verbose_name=_("landline number"))
    mobile = models.CharField(max_length=150, verbose_name=_("Phone number"))
    email = models.EmailField(verbose_name=_("Email"))
    score = models.IntegerField(verbose_name=_("Score"))
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ["first_name", "regdate"]
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


class Teacher(models.Model):
    nat_code = models.CharField(
        max_length=150, verbose_name=_("Teacher's national code")
    )
    first_name = models.CharField(max_length=150, verbose_name=_("Teacher's name"))
    last_name = models.CharField(max_length=150, verbose_name=_("Teacher's last name"))
    birthday_date = models.DateField(verbose_name=_("Date of birth"))
    telephone = models.CharField(max_length=150, verbose_name=_("landline number"))
    mobile = models.CharField(max_length=150, verbose_name=_("Phone number"))
    email = models.EmailField(verbose_name=_("Email"))
    field = models.CharField(max_length=150, verbose_name=_("Field of Study"))
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


class Level(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name=_("Section name"))
    regdate = models.DateField(null=True, verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["regdate"]
        verbose_name = _("Level")
        verbose_name_plural = _("Levels")


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name of Course"))
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, verbose_name=_("Section")
    )
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["level"]
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")


class Term(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Term name"))
    startDate = models.DateField(verbose_name=_("Start date"))
    endDate = models.DateField(verbose_name=_("End date"))
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")


class StudentTerm(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name=_("Student")
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Course")
    )
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name=_("Term"))
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.student.last_name

    class Meta:
        verbose_name = _("Student Term")
        verbose_name_plural = _("Student Terms")