from django.db import models

# creating a Post model class


class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    # assigning post name as self
    def __str__(self):
        return self.text
