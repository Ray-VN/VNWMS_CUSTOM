from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Warehouse(models.Model):
    wh_code = models.CharField(max_length=20, primary_key=True)
    wh_name = models.CharField(max_length=100)
    wh_bg = models.CharField(max_length=100, blank=True, null=True)
    wh_comment = models.CharField(max_length=100, blank=True, null=True)
    create_at = timezone.now(),
    create_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='warehouse_create_by',
        null=True, blank=True
    )