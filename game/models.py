from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Game(models.Model):
        player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
        date_created = models.DateTimeField(auto_now_add=True)
        score = models.IntegerField()
        
        def __str__(self):
                return f'Game by {self.player}'
