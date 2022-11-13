from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    text = models.TextField()
    slug = models.SlugField("Slug", max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.text


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
