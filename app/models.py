from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/")


