from django.db import models

# Create your models here.
class GetInTouch(models.Model):
    name=models.CharField(max_length=150, blank=False, null=False)
    email=models.CharField(max_length=150, blank=False, null=False)
    subject=models.CharField(max_length=150, blank=False, null=False)
    message=models.TextField(max_length=150, blank=False, null=False)
    sent_at=models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return self.name