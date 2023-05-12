from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'author', default= 1)
    addressee = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'receiver')
    text = models.CharField(max_length= 255)
    datetime = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.text
