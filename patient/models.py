from __future__ import unicode_literals

from django.db import models

#external models
from person.models import Person, PersonDemographic, PersonContact, PersonRelative

# Create your models here.

class Patient(Person):
    pass

class PatientDemographic(PersonDemographic):
    pass

class PatientContact(PersonContact):
    pass

class PatientRelative(PersonRelative):
    pass
