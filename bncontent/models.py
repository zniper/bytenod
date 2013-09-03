from django.db import models

class NormalPost(models.Model):
    title = models.CharField(max_length=256)
    brief = models.TextField(blank=True, null=True)
    post_type = models.IntegerField()
    url = models.CharField(max_length=256, blank=True, null=True)
    tags = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey('PostCategory')

class PostCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


