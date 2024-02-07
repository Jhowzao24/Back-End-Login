from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=150, unique=True);
    password = models.CharField(max_length=180);
    
    def __str__(self):
        return self.Username