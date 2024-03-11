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
        return self.first_name