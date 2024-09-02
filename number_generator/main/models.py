from django.db import models

class RandomNumber(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)