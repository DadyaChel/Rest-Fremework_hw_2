from django.db import models


class Positions(models.Model):
    position = models.CharField(max_length=250)
    department = models.CharField(max_length=222)

    def __str__(self):
        return self.position


class Employee(models.Model):
    FIO = models.CharField(max_length=222)
    date_birth = models.DateField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    zp = models.IntegerField()

    def __str__(self):
        return self.FIO