from django.db import models # new

class Post(models.Model): # new
    text = models.TextField()

    def __str__(self):
        return self.text
