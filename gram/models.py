from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImagePost(models.Model):
    img_title = models.CharField(max_length =60)
    img_desc = models.TextField(
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'images/')

class Profile(models.Model):
    bio = models.TextField()
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photo/')

class Comments(models.Model):
    comment = models.TextField()
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    image =  models.ForeignKey(ImagePost,on_delete=models.CASCADE)