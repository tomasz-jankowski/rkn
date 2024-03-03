from enum import Enum


class SocietyTypes(Enum):
    UNDEFINED = 'undefined'
    CLUB = 'club'
    ORGANIZATION = 'organization'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
