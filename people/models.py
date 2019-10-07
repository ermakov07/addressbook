from django.db import models

class ListPeople(models.Model):
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    ot = models.CharField(max_length=50)
    addr = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    note = models.TextField(null=True, blank=True)