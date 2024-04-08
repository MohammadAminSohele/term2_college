from django.db import models

# Create your models here.

class Student(models.Model):
    nat_code = models.CharField(max_length = 150,verbose_name='کد ملی')
    first_name = models.CharField(max_length = 150,verbose_name='نام دانشجو')
    last_name = models.CharField(max_length = 150,verbose_name='نام خانوادگی دانشجو')
    birthday_date = models.DateField(verbose_name='تاریخ تولد دانشجو')
    telephone = models.CharField(max_length = 150,verbose_name='شماره تلفن ثابت دانشجو')
    mobile = models.CharField(max_length = 150,verbose_name='شماره تلفن همراه دانشجو')
    email = models.EmailField(verbose_name='ایمیل دانشجو')
    score = models.IntegerField(verbose_name='نمره دانشجو')
    regdate = models.DateField(verbose_name='تاریخ ثبت دانشجو')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.last_name
    
class Teacher(models.Model):
    nat_code = models.CharField(max_length = 150,verbose_name='کد ملی استاد')
    first_name = models.CharField(max_length = 150,verbose_name='نام استاد')
    last_name = models.CharField(max_length = 150,verbose_name='نام خانوادگی استاد')
    birthday_date = models.DateField(verbose_name='تاریخ تولد استاد')
    telephone = models.CharField(max_length = 150,verbose_name='شماره تلفن ثابت استاد')
    mobile = models.CharField(max_length = 150,verbose_name='شماره تلفن استاد')
    email = models.EmailField(verbose_name='ایمیل استاد')
    field = models.CharField(max_length = 150,verbose_name='رشته تحصیلی استاد')
    regdate = models.DateField(verbose_name='تاریخ ثبت استاد')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.last_name

class Level(models.Model):
    name = models.CharField(max_length = 150,null=True,verbose_name='نام مقطع')
    regdate = models.DateField(null=True,verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 150,verbose_name='نام درس')
    level = models.ForeignKey(Level, on_delete=models.CASCADE,verbose_name='مقطع')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length = 150,verbose_name='نام ترم')
    startDate = models.DateField(verbose_name='تاریخ شروع')
    endDate = models.DateField(verbose_name='تاریخ پایان')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

class StudentTerm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='دانشجو')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='درس')
    term = models.ForeignKey(Term, on_delete=models.CASCADE,verbose_name='ترم')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.student.last_name