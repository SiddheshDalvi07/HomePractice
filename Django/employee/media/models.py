from django.db import models

# Create your models here.
class MediaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def audio(self):
        return self.get_queryset().filter(type='Audio')

    def video(self):
        return self.get_queryset().filter(type='Video')

    def images(self):
        return self.get_queryset().filter(type='Image')

class Media(models.Model):
    name = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Image', 'Image'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    format = models.CharField(max_length=10)
    size = models.IntegerField()  # Size in MB
    duration_secs = models.IntegerField(default=0)

    objects = MediaManager()

    def __str__(self):
        return self.name