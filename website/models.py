from django.db import models
from django.contrib.auth.models import User


# create model here
class MyApp(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='my_apps')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_app')

    def __str__(self):
        return f'MyApp {self.id} {self.name}'

    """Every time we create something, it will have its own id and name
    ex: If we create app test app it will be -> MyApp 1 test app"""

    class Meta:
        verbose_name_plural = 'My apps'
        ordering = ['name']
