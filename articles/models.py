import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    name = models.CharField(
        max_length=25,
        unique=True,
    )
    
    description = models.TextField(
        max_length=50,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

class Article(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
    )

    title = models.CharField(
        max_length=25,
        unique=True,
    )  

    description = models.TextField(
        max_length=100,
    )   

    category = models.ForeignKey(
        Category,
        related_name='category',
        null=True,
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )