from django.db import IntegrityError
from django.test import TestCase

from accounts.models import Account
from budgets.models import Budget
from faculties.models import Faculty
from societies.models import Society


class BudgetTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(name='name')
        faculty = Faculty.objects.create(name='name')
        self.society = Society.objects.create(name='name', faculty=faculty)
        self.budget = Budget.objects.create(
            account=self.account,
            society=self.society,
        )

    def test_budget_is_created(self):
        self.assertIsInstance(self.budget, Budget)

    def test_budget_has_no_account(self):
        with self.assertRaises(IntegrityError):
            Budget.objects.create(
                society=self.society,
            )

    def test_budget_has_no_society(self):
        with self.assertRaises(IntegrityError):
            Budget.objects.create(
                account=self.account,
            )
