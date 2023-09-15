from django.db import models

# Create your models here.
class Video(models.Model):
    description=models.CharField(max_length=200)
    video=models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return self.description
    
    