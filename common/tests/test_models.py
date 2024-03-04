from django.db import IntegrityError
from django.test import TestCase

from common.models import TimeStampedModel, TimeStampedSluggifiedModel


class TimeStampedTestModel(TimeStampedModel):
    class Meta:
        app_label = 'common'


class TimeStampedSluggifiedTestModel(TimeStampedSluggifiedModel):
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
            name="name"
        )

    def test_object_is_created(self):
        obj = TimeStampedSluggifiedTestModel.objects.get(
            name="name"
        )
        self.assertIsInstance(obj, TimeStampedSluggifiedTestModel)

    def test_object_has_valid_slug(self):
        obj = TimeStampedSluggifiedTestModel.objects.create(
            name="Name of Instance"
        )
        self.assertEqual(obj.slug, "name-of-instance")

    def test_object_str_method(self):
        name = "Name of Instance"
        obj = TimeStampedSluggifiedTestModel.objects.create(
            name=name
        )
        self.assertEqual(str(obj), name)

    def test_obj_has_non_unique_name(self):
        with self.assertRaises(IntegrityError):
            TimeStampedSluggifiedTestModel.objects.create(
                name="name",
            )
