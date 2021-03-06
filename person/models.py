from __future__ import unicode_literals
from datetime import date, datetime
from django.db import models

# Create your models here.

    
class Gender(models.Model):    
    name = models.CharField("Gender Name", blank=True, max_length=200)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Gender"

        
class MaritalStatus(models.Model):
    name = models.CharField("Status", max_length=200)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Marital Status'
        verbose_name = 'Marital Status'
        
class Religion(models.Model):
    name = models.CharField("Religion Name", max_length=200)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}".format(self.name)
    
class Prefix(models.Model):
    name = models.CharField("Prefix Name", max_length=200)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Prefixes"

class Relationship(models.Model):
    name = models.CharField("Relationship Name", max_length=200)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}".format(self.name)
        
class Person(models.Model):
    surname = models.CharField("Surname", max_length=200)
    firstname = models.CharField("Firstname", max_length=200)
    othername = models.CharField("Othername", blank=True, max_length=200)
    prefix = models.ForeignKey(Prefix)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    id_number = models.CharField("ID Number", unique=True, max_length=200, editable=False, default='00-00-00')

        
    def __str__(self):
        return "{} {}".format(self.surname, self.firstname)

    class Meta:
        get_latest_by = 'date_created'
    
class PersonDemographic(models.Model):
    person = models.ForeignKey(Person)
    gender = models.ForeignKey(Gender)
    birthdate = models.DateField("Date of Birth")
    marital_status = models.ForeignKey(MaritalStatus)
    religion = models.ForeignKey(Religion)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return "{}".format(self.person)

    class Meta:
        verbose_name = "Person Demographic"

        
class PersonPhoto(models.Model):
    person = models.ForeignKey(Person)
    photo = models.CharField("Picture", max_length=300)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return "{}".format(self.person)

    class Meta:
        verbose_name = "Person Photo"

        
class PersonContact(models.Model):
    person = models.ForeignKey(Person)
    mobile = models.CharField("Mobile Number", blank=True, max_length=200)
    telephone = models.CharField("Telephone", blank=True, max_length=200)
    alt_mobile = models.CharField("Alternate Mobile Number", blank=True, max_length=200)
    email = models.EmailField(blank=True)
    mailing_address = models.TextField("Mailing Address", blank=True, max_length=200)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return "{}".format(self.person)

class PersonRelative(PersonContact):    
    full_name = models.CharField("Relative Name", max_length=200)
    relationship = models.ForeignKey(Relationship)
