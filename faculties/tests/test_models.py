from django.test import TestCase

from faculties.models import Faculty


class FacultyTestCase(TestCase):
    def setUp(self):
        Faculty.objects.create(name="name")

    def test_faculty_is_created(self):
        faculty = Faculty.objects.get(name="name")
        self.assertIsInstance(faculty, Faculty)
