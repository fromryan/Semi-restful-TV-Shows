from __future__ import unicode_literals
from django.db import models


class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description is optional, but should be at least 10 characters if provided"
        if Show.objects.filter(title = postData['title']):
            errors["title"] = "Title must be unique."
        return errors



class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    released_date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Show ID: ({self.id})| Title: {self.title}| Network: {self.network}| Release Date: {self.release_date}| Description: {self.description} ||"


