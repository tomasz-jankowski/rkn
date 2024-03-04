from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from accounts.models import Account


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(name='name')

    def test_account_is_created(self):
        account = Account.objects.get(name='name')
        self.assertIsInstance(account, Account)

    def test_account_str_method(self):
        account = Account.objects.get(name="name")
        self.assertEqual(str(account), account.name)

    def test_account_has_non_unique_name(self):
        with self.assertRaises(IntegrityError):
            Account.objects.create(name='name')

    def test_accounts_has_invalid_type(self):
        account = Account.objects.create(
            name='test',
            type='INVALID'
        )
        self.assertRaises(ValidationError, account.full_clean)
