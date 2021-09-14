from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.db.models.signals import post_save 

        
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio =  models.TextField(max_length=200)
    user =  models.OneToOneField(User, on_delete=models.CASCADE,  default = "")


    def __str__(self):
        return self.bio

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    @classmethod
    def delete(cls,id):
        cls.objects.delete(id = id)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    caption = models.TextField(max_length=200)
    comments = models.TextField(max_length=200)
    likes = models.ManyToManyField(User, related_name="post_likes")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default = "")

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

