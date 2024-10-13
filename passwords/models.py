from django.db import models


class PasswordCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Password(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False, blank=False)
    username = models.CharField(max_length=255, unique=False, null=True, blank=True)
    password = models.CharField(max_length=255, unique=False, null=True, blank=True)
    category = models.ForeignKey(
        PasswordCategory, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name, self.username
