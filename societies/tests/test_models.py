from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from faculties.models import Faculty
from societies.models import Society


class SocietyTestCase(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="name")
        Society.objects.create(
            name="name",
            email="student@student.put.poznan.pl",
            supervisor_email="supervisor@put.poznan.pl",
            faculty=self.faculty
        )

    def test_society_is_created(self):
        society = Society.objects.get(name="name")
        self.assertIsInstance(society, Society)

    def test_society_has_no_faculty(self):
        with self.assertRaises(IntegrityError):
            Society.objects.create(
                name="test",
                email="email@example.com",
            )

    def test_society_has_invalid_email(self):
        society = Society.objects.create(
            name="test",
            email="email@example.com",
            faculty=self.faculty
        )
        self.assertRaises(ValidationError, society.full_clean)

    def test_society_has_invalid_supervisor_email(self):
        society = Society.objects.create(
            name="test",
            supervisor_email="email@example.com",
            faculty=self.faculty
        )
        self.assertRaises(ValidationError, society.full_clean)

    def test_society_has_invalid_type(self):
        society = Society.objects.create(
            name="test",
            type="INVALID",
            faculty=self.faculty
        )
        self.assertRaises(ValidationError, society.full_clean)
