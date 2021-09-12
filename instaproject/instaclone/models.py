from typing import BinaryIO
from django.db import models
from django.contrib.auth.models import User


        
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    bio =  models.TextField(max_length=200)

    def __str__(self):
        return self.bio

    def save(self):
        self.save()

    @classmethod
    def update(cls,id):
        profile = cls.objects.update(id = id)
        return profile
    @classmethod
    def delete(cls,id):
        cls.objects.delete(id = id)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    caption = models.TextField(max_length=200)
    comments = models.TextField(max_length=200)
    likes = models.ManyToManyField(User, related_name="post_likes")
    comments = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def number_of_likes(self):
        return self.likes.count()
    
    @classmethod
    def get_image_by_id(cls,id):
        photo = cls.objects.get(id = id)
        return photo

    @classmethod
    def delete_image(cls,id):
        cls.objects.delete(id = id)

    @classmethod
    def update_caption(cls,id):
        photo = cls.objects.update(id = id)
        return photo

