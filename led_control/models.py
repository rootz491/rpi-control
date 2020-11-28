from django.db import models

# Create your models here.

class led(models.Model):
        is_active = models.BooleanField(default=False)
        message = models.CharField(default='user has not provided any message', max_length=100)
        active_on = models.DateTimeField(auto_now_add=True)

        # reverse the order of DateTimeField so i can get the latest data
        class Meta:
                ordering = ['-active_on']

        def __str__(self):
                if self.is_active:
                        return 'GLOWING'
                return 'NOT GLOWING'

