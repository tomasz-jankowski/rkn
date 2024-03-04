from _decimal import Decimal

from django.db import IntegrityError, DataError
from django.test import TestCase

from common.models import TimeStampedModel, TimeStampedSluggifiedModel, FinanceModel


class TimeStampedTestModel(TimeStampedModel):
    class Meta:
        app_label = 'common'


class TimeStampedSluggifiedTestModel(TimeStampedSluggifiedModel):
    class Meta:
        app_label = 'common'


class FinanceTestModel(FinanceModel):
    class Meta:
        app_label = 'common'


class TimeStampedModelTestCase(TestCase):
    def test_time_stamped_model_is_created(self):
        model = TimeStampedTestModel.objects.create()
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)


class TimeStampedSluggifiedTestCase(TestCase):
    def setUp(self):
        TimeStampedSluggifiedTestModel.objects.create(
            name='name'
        )

    def test_object_is_created(self):
        obj = TimeStampedSluggifiedTestModel.objects.get(
            name='name'
        )
        self.assertIsInstance(obj, TimeStampedSluggifiedTestModel)

    def test_object_has_valid_slug(self):
        obj = TimeStampedSluggifiedTestModel.objects.create(
            name='Name of Instance'
        )
        self.assertEqual(obj.slug, 'name-of-instance')

    def test_object_str_method(self):
        name = 'Name of Instance'
        obj = TimeStampedSluggifiedTestModel.objects.create(
            name=name
        )
        self.assertEqual(str(obj), name)

    def test_obj_has_non_unique_name(self):
        with self.assertRaises(IntegrityError):
            TimeStampedSluggifiedTestModel.objects.create(
                name='name',
            )


class FinanceModelTestCase(TestCase):
    def test_obj_is_created(self):
        instance = FinanceTestModel.objects.create(
            requested=1.2,
            granted=1.23,
            spent=1.234,
            left=123456.789,
        )
        saved = FinanceTestModel.objects.get(pk=instance.pk)

        self.assertIsInstance(instance, FinanceTestModel)
        self.assertEqual(saved.requested, Decimal('1.20'))
        self.assertEqual(saved.granted, Decimal('1.23'))
        self.assertEqual(saved.spent, Decimal('1.23'))
        self.assertEqual(saved.left, Decimal('123456.79'))

    def test_obj_has_too_many_digits(self):
        with self.assertRaises(DataError):
            FinanceTestModel.objects.create(
                requested=112233445566778899,
            )
