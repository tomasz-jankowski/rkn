from enum import Enum


class AccountTypes(Enum):
    STATUTORY = 'statutory'
    ADDITIONAL = 'additional'
    SPONSORSHIP = 'sponsorship'
    OTHER = 'other'
    GRANT = 'grant'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
