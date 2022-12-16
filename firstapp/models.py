from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    DoesNotExist = models.Manager # на работу не влияет, чтобы pycharm не выдавало ошибку

class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # CASCADE, PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2)

