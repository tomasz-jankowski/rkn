from django.db import models

from common.models import TimeStampedSluggifiedModel
from common.validators import PutDomainValidator
from faculties.models import Faculty
from .enums import SocietyTypes


class Society(TimeStampedSluggifiedModel):
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(null=True, blank=True, validators=[PutDomainValidator()])
    leader = models.CharField(null=True, blank=True)
    supervisor = models.CharField(null=True, blank=True)
    supervisor_email = models.CharField(null=True, blank=True, validators=[PutDomainValidator()])
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(choices=SocietyTypes.choices(), default=SocietyTypes.UNDEFINED)
    visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    logo = models.ImageField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def remove_on_image_update(self):
        try:
            obj = Society.objects.get(id=self.id)
        except Society.DoesNotExist:
            return
        if obj.logo and (not self.logo or obj.logo != self.logo):
            obj.logo.delete(save=False)

    def delete(self, *args, **kwargs):
        self.logo.delete()
        return super(Society, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.remove_on_image_update()
        return super(Society, self).save(*args, **kwargs)

    class Meta:
        db_table = 'societies'
        verbose_name_plural = 'societies'
