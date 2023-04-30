from django.db import models
from users.models import User


class Articles(models.Model):
    title = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)