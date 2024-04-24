from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(
        get_user_model(), blank=False,
        on_delete=models.CASCADE, verbose_name=_("User"),
    )
    nat_code = models.CharField(
        max_length=10, verbose_name=_("Student's national code"),
        blank=False, null=False,
    )
    birthday_date = models.DateField(verbose_name=_("Date of birth"))
    telephone = models.CharField(max_length=11, verbose_name=_("landline number"))
    mobile_regex = RegexValidator(
        regex=r"^09\d{2}\s*?\d{3}\s*?\d{4}$", message=_("Invalid phone number."),
    )
    mobile = models.CharField(max_length=11, verbose_name=_("Phone number"), validators=[mobile_regex], )
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return f"{self.user.last_name} - {self.user.first_name}"

    class Meta:
        ordering = ["user__first_name", "regdate"]
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


class DegreeOfEducation(models.Model):
    name = models.TextField(
        max_length=200, verbose_name=_("Name of degree"),
        blank=False, null=False,
    )
    study = models.TextField(
        max_length=200, verbose_name=_("Field of Study"),
        blank=False, null=False,
    )

    def __str__(self):
        return f"{self.name}-{self.study}"
    
    class Meta:
        verbose_name = _("DegreeOfEducation")
        verbose_name_plural = _("DegreeOfEducations")


class Teacher(models.Model):
    user = models.ForeignKey(
        get_user_model(), blank=False,
        on_delete=models.CASCADE, verbose_name=_("User"),
    )
    nat_code = models.CharField(
        max_length=10, verbose_name=_("Teacher's national code")
    )
    birthday_date = models.DateField(verbose_name=_("Date of birth"))
    telephone = models.CharField(max_length=11, verbose_name=_("landline number"))
    mobile_regex = RegexValidator(
        regex=r"^09\d{2}\s*?\d{3}\s*?\d{4}$", message=_("Invalid phone number."),
    )
    mobile = models.CharField(max_length=11, verbose_name=_("Phone number"))
    field = models.ForeignKey(
        DegreeOfEducation, on_delete=models.CASCADE,
        verbose_name=_("Degree Of Education"),
    )
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.user.last_name

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
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE,
        null=False, default=None,
        verbose_name=_("Teacher"), related_name="courses",
    )
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, 
        verbose_name=_("Section"), null=False,
    )
    regdate = models.DateField(verbose_name=_("Date of Registration"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return f"{self.name} - {self.teacher.user.first_name}-{self.teacher.user.last_name}"

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
        return self.student.user.last_name

    class Meta:
        verbose_name = _("Student Term")
        verbose_name_plural = _("Student Terms")
