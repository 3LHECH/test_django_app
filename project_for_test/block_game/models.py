from django.db import models

# Create your models here.
class Score(models.Model):
    score = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            existing = Score.objects.first()
            if existing:
                self.pk = existing.pk  
        super().save(*args, **kwargs)