from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_nam=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.TextField()
    question=models.TextField()
    
    def __str__(self):
        return self.first_namefrom
