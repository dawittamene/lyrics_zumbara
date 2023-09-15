from django.db import models

# Create your models here.
class Video(models.Model):
    description=models.CharField(max_length=200)
    name=models.CharField(max_length=200,unique=True, null=True)
    video=models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return self.description
    
    