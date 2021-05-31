from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
class Lead (models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.firstName} {self.lastName}"


