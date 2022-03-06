from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
# Create your models here.
class TodoApp(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default = False)

    
