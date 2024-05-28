from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
        
        ROLE_CHOICES = {
		"ME" : "Member",
		"GU" : "Guest",
	}
        
        profil_photo = models.ImageField(null=True)
        birthday = models.DateField(null=True, blank=True)
        role = models.CharField(max_length=5, choices=ROLE_CHOICES)
        
        def resize_photo(self):
                image_max_size = (800, 800)
                image = Image.open(self.profil_photo)
                image.thumbnail(image_max_size)
                image.save(self.profil_photo.path)
        
        def save(self, *args, **kwargs):
                super().save(*args, **kwargs)
                if self.profil_photo:
                        self.resize_photo()
        
        def __str__(self):
                return self.username