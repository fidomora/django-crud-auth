from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(("title"), max_length=100) 
    description = models.TextField(("description"), blank=True, null=True)
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)
    datecompleted = models.DateTimeField(("completed"), auto_now=False, auto_now_add=False, null=True, blank=True)
    important = models.BooleanField(("important"), default=False)
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' by '+ self.user.username