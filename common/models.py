from django.db import models
from django.db.models import SlugField
from django.utils.text import slugify
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
    slug = SlugField(blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class FinanceModel(TimeStampedModel):
    requested = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, editable=False)
    granted = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, editable=False)
    spent = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, editable=False)
    left = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, editable=False)

    class Meta:
        abstract = True
