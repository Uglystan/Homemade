from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction

class Task(models.Model):
        
        title = models.CharField(max_length=128)
        description = models.CharField(max_length=2000, null=True, blank=True)
        author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks_authored')
        target = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks_received')
        finish = models.BooleanField(default=False)
        date_created = models.DateTimeField(auto_now_add=True)
        date_updated = models.DateTimeField(auto_now=True)
        
        @transaction.atomic
        def done(self):
                if self.finish == True:
                        return
                self.finish = True
                self.save()

        def __str__(self):
                return self.title