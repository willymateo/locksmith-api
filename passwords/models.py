from django.db import models
import uuid


class PasswordCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Password(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=False, null=False, blank=False)
    username = models.CharField(max_length=255, unique=False, null=True, blank=True)
    password = models.CharField(max_length=255, unique=False, null=True, blank=True)
    category = models.ForeignKey(
        PasswordCategory,
        on_delete=models.PROTECT,
        related_name="passwords",
        null=True,
        db_column="password_category_id",
    )

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name, self.username
