from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
    

class Question(models.Model):
    choice = models.ForeignKey(Category, on_delete=models.CASCADE)
    quiz_image = models.ImageField(upload_to ='quiz_image/', blank=True)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100, blank=True)
    option_two = models.CharField(max_length=100, blank=True)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question