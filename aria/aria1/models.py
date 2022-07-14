from django.db import models

# Create your models here.
class Contact(models.Model):
    # contact act as a table
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    text =  models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.email