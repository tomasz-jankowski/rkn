from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class PutDomainValidator(EmailValidator):
    def __init__(self):
        self.message = "Email is not a PUT domain email!"
        self.domain_allowlist = [
            "put.poznan.pl",
            "student.put.poznan.pl",
            "rkn.put.poznan.pl",
            "doctorate.put.poznan.pl",
        ]
        super().__init__()

    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, PutDomainValidator) and super().__eq__(other)
