from common.models import TimeStampedSluggifiedModel


class Faculty(TimeStampedSluggifiedModel):
    class Meta:
        db_table = 'faculties'
        verbose_name_plural = 'faculties'
