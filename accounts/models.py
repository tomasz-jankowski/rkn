from django.db import models

from accounts.enums import AccountTypes
from common.models import FinanceModel


class Account(FinanceModel):
    name = models.CharField(unique=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    active = models.BooleanField(default=False)
    type = models.CharField(choices=AccountTypes.choices())
    unlimited = models.BooleanField(default=False)
    amount_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'accounts'
