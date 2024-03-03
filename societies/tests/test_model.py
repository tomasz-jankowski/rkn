from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from societies.models import Society


class SocietyTestCase(TestCase):
    def setUp(self):
        Society.objects.create(
            name="name",
            email="student@student.put.poznan.pl",
            leader="leader",
            supervisor_email="supervisor@put.poznan.pl"
        )

    def test_society_has_valid_slug(self):
        society = Society.objects.create(
            name="Name of Society",
            leader="test"
        )
        self.assertEqual(society.slug, "name-of-society")

    def test_society_is_created(self):
        society = Society.objects.get(name="name")
        self.assertIsInstance(society, Society)

    def test_society_has_non_unique_name(self):
        with self.assertRaises(IntegrityError):
            Society.objects.create(
                name="name",
                leader="test"
            )

    def test_society_has_invalid_email(self):
        society = Society.objects.create(
            name="test",
            leader="test",
            email="email@example.com"
        )
        self.assertRaises(ValidationError, society.full_clean)

    def test_society_has_invalid_supervisor_email(self):
        society = Society.objects.create(
            name="test",
            leader="test",
            supervisor_email="email@example.com"
        )
        self.assertRaises(ValidationError, society.full_clean)

    def test_society_has_invalid_type(self):
        society = Society.objects.create(
            name="test",
            leader="test",
            type="INVALID"
        )
        self.assertRaises(ValidationError, society.full_clean)


