from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    city = models.CharField(max_length=100)
    address = models.TextField(default="")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desctiption": self.description,
            "city": self.city,
            "address": self.address
        }

class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = 'Vacancies'
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "salary": self.salary
        }