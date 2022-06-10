from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User (AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    email = models.EmailField(verbose_name="Email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"
    
    def __repr__(self):
        return f"USER [ID: {self.pk}]"


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.name: 
            self.name = self.name.strip()
        return super().save(*args, **kwargs)