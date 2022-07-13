from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from rest_framework import serializers
from vacancy.models import Vacancy


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    city = models.CharField(max_length=65)
    phone_num = PhoneNumberField()
    sex = models.CharField(max_length=65)
    birth_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CV(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    birth_date = models.DateField()
    mobile_num = models.CharField(max_length=25)
    email = models.EmailField()
    registration = models.CharField(max_length=100)
    sex = models.CharField(max_length=65)
    position = models.CharField(max_length=65)
    sphere = models.CharField(max_length=100)
    min_salary = models.IntegerField()
    busyness = models.CharField(max_length=65, default='')
    work_graph = models.CharField(max_length=65)
    about = models.TextField()
    views = models.IntegerField(default=0)
    suitable_vacancies = models.ManyToManyField(Vacancy, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}\'s CV {self.pk}'


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'


class CVAttr(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True, blank=True)


class KnownLanguage(CVAttr):
    language = models.CharField(max_length=25)
    level = models.CharField(max_length=65)


class KnownProgram(CVAttr):
    program = models.CharField(max_length=65)


class WorkExperience(CVAttr):
    position = models.CharField(max_length=65)
    org_name = models.CharField(max_length=100)
    responsibilities = models.TextField()
    start_year = models.CharField(max_length=65)
    end_year = models.CharField(max_length=65)

    def __str__(self):
        return f'WorkExpr cv:{self.cv.id}'


class Education(CVAttr):
    degree = models.CharField(max_length=65)
    establishment = models.CharField(max_length=65)
    faculty = models.CharField(max_length=65)
    specialization = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()


class Response(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)


class ChosenVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class ChosenCv(models.Model):
    hirer = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)