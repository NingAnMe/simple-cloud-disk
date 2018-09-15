from django.db import models


# Create your models here.
class Video(models.Model):
    video_name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date create')
    video_path = models.CharField(max_length=200)

    def __str__(self):
        return self.video_name
