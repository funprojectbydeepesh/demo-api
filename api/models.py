from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



#address
class Address(TimeStampedModel):
    class ProvinceChoice(models.TextChoices):
        GANDAKI = ('Gandaki Province', 'Gandaki Province')
        PROVINCENO1 = ('Province No. 1', 'Province No. 1')
        MADHESH = ('Madhesh Province', 'Madhesh Province')
        BAGMATI = ('Bagmati Province', 'Bagmati Province')
        LUMBINI = ('Lumbini Province', 'Lumbini Province')
        KARNALI = ('Karnali Province', 'Karnali Province')
        SUDURPASCHIM = ('Sudurpaschim Province', 'Sudurpashcim Province')

    province = models.CharField(max_length=30,
                                blank=True,
                                choices=ProvinceChoice.choices,
                                verbose_name=_("Province"))
    district = models.CharField(max_length=40,
                                blank=True,
                                verbose_name=_("District"))
    city = models.CharField(max_length=40, blank=True, verbose_name=_("City"))
    tole = models.CharField(max_length=80, blank=True, verbose_name=_("Tole"))
    


    def __str__(self):
         return f'{self.province} + {self.district}'


# Student 

class Student(TimeStampedModel):
    class GradeChoice(models.TextChoices):
        A = ('A', ' A')
        B = ('B', 'B')
        C = ('C', 'C')
        D = ('D', 'D')
        E = ('E', 'E')
        F = ('F', 'F')

    name = models.CharField(max_length=200, 
                            blank=True, 
                            null=True, 
                            verbose_name=_('Name')
                        )
    age = models.IntegerField(blank=True,
                              null=True,
                              verbose_name=_('Age')
                              )
    address = models.ForeignKey(Address, 
                                on_delete=models.CASCADE,
                                related_name='Address')
    grade = models.CharField( max_length=20,
                             blank=True,
                             choices=GradeChoice.choices,
                             verbose_name=_('Grade'))
    major = models.CharField(max_length=200,
                             blank=True,
                             verbose_name=_('Major'))
    
    def __srt__(self):
        return self.name