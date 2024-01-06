from django.db import models

class TextSample(models.Model):
    text = models.TextField()
    is_phishing = models.BooleanField(null=True, blank=True)
