from django.db import models

# Create your models here.
class graingerMajor(models.Model):
    name = models.CharField(max_length=100)

class lasMajor(models.Model):
    name = models.CharField(max_length=100)

class giesMajor(models.Model):
    name = models.CharField(max_length=100)

class fileUploadG(models.Model):
    courseTag = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to="files/")

class fileUploadL(models.Model):
    courseTag = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to="files/")

class fileUploadB(models.Model):
    courseTag = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to="files/")

class contributors(models.Model):
    creatorName = models.CharField(max_length=100)
