from django.db import models

# Create your models here.
class Subsribers (models.Model):
    email = models.CharField (blank = False, null = False, help_text = "Email", max_length = 100)
    full_name = models.CharField (blank = False, null = False, help_text = "First and Last name", max_length = 100)
    
    def __str__(self):
        return self.full_name