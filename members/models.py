from django.db import models

class Member(models.Model):
  header = models.TextField()
  img_url = models.TextField()
