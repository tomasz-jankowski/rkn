from django.db import models

from accounts.models import Account
from common.models import FinanceModel
from societies.models import Society


class Budget(FinanceModel):
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)

    class Meta:
        db_table = 'budgets'
