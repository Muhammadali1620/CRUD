from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from apps.category.models import Category


class Todos(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ManyToManyField(User)

    done = models.BooleanField(default=False)
    done_at = models.DateField(blank=True, null=True)

    start_date = models.DateField(default=now)
    days = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title