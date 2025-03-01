from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add repopulates the field wheneer we make a new version or new instance of te note object
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        # user will have a one to many relationship with notes having the foreign key to link to the user field
        User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
