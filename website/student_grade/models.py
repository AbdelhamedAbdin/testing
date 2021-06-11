from django.db import models
import re


class Student(models.Model):
    student = models.IntegerField(blank=False)
    grade = models.CharField(max_length=10)
    gender = models.CharField(max_length=3)

    def __str__(self):
        return str(self.student)

    def get_absolute_url(self):
        return self.pk


class Character(models.Model):
    character = models.CharField(max_length=2)
    regularity = models.CharField(max_length=5)
    complexity = models.CharField(max_length=2)

    def __str__(self):
        return self.character

    def get_absolute_url(self):
        return self.pk


class Response(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    correct = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.correct)

    def get_absolute_url(self):
        return self.pk

    def modifyErrorClass(self):
        for errors in self.student.error_set.all():
            if errors.error_class is not None:
                return errors.error_class

    def modifyErrorNumber(self):
        for errors in self.student.error_set.all():
            return errors.error_number

    def modifyErrorUnit(self):
        for errors in self.student.error_set.all():
            if errors.error_class is not None:
                return errors.error_unit

    def modifyErrorType(self):
        for errors in self.student.error_set.all():
            if errors.error_class is not None:
                return errors.error_type


class Error(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    error_class = models.CharField(max_length=5, blank=True, null=True)
    error_number = models.CharField(max_length=5)
    error_unit = models.CharField(max_length=20, blank=True, null=True)
    error_type = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.student_id)

    def get_absolute_url(self):
        return str(self.pk)


class History(models.Model):
    user_ip = models.CharField(max_length=15, default='127.0.0.1')
    action = models.CharField(max_length=15, default='visit')
    visit_date = models.DateField(auto_now_add=True)
    country_ip = models.CharField(max_length=30, default='Unknown')
    city_ip = models.CharField(max_length=30, default='Unknown')

    def __str__(self):
        return self.action
