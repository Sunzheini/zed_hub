from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


class TemplateModel(models.Model):
    MAX_NAME_LENGTH = 99
    MIN_NAME_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=False, null=False,
        unique=True,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
        ],
    )

    description = models.TextField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name[0:30]}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
