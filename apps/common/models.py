from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from unidecode import unidecode


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def _slugify(content: str) -> str:
    return slugify(unidecode(content))


class TimeStampedSluggifiedModel(TimeStampedModel):
    name = models.CharField(unique=True)
    slug = AutoSlugField(populate_from='name', slugify_function=_slugify, overwrite=True)

    class Meta:
        abstract = True
