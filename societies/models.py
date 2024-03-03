from common.models import TimeStampedSluggifiedModel
from django.db import models

from common.validators import PutDomainValidator
from .enums import SocietyTypes


class Society(TimeStampedSluggifiedModel):
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(null=True, blank=True, validators=[PutDomainValidator()])
    leader = models.CharField(null=True, blank=True)
    supervisor = models.CharField()
    supervisor_email = models.CharField(null=True, blank=True, validators=[PutDomainValidator()])
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(choices=SocietyTypes.choices(), default=SocietyTypes.UNDEFINED)
    visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    logo_path = models.CharField(null=True, blank=True)

    class Meta:
        db_table = 'societies'
        verbose_name_plural = 'societies'
