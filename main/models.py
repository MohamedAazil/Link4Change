from django.db import models

class Entrepreneur(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=255)  # Comma-separated tags

    def __str__(self):
        return self.title

class Investor(models.Model):
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)  # Comma-separated tags

    def __str__(self):
        return self.name
