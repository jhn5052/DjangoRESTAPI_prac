from django.db import models

# Create your models here.
class ClassBlog(models.Model):
    title = models.CharField(max_length = 100)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    body = models.TextField()

    def __str__(self):
        return self.title