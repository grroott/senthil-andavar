from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return f'{self.subject}'