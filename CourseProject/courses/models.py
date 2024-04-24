from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    published_by = models.PositiveIntegerField(null=True, blank=True)
    # user_id del servicio 1
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title