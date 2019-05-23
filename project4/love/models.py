from django.db import models

class Calculator(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=64)
  second_name = models.CharField(max_length=64)
  percentage = models.FloatField(null=True)
  result = models.TextField(blank=True)
  message = models.TextField(blank=True)

  def __str__(self):
    return f"{self.id} {self.first_name} - {self.second_name} -{self.percentage}"

class Comment(models.Model):
  id = models.AutoField(primary_key=True)
  author = models.CharField(max_length=64)
  text = models.TextField(blank=False)
  date = models.DateField(auto_now=True)

  def __str__(self):
    return f"{self.id} {self.date} - {self.author}"
