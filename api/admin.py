from django.contrib import admin
from .models import Student,Address

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name',
              'age',
              'grade',
              'address',
              'major')
    list_display = ('name',
                    'age',
                    'grade',
                    'address',
                    'major')
    search_fields = ('name', 
                     ' grade',
                     'major')


@admin.register(Address)
class Address(admin.ModelAdmin):
    fields = ('province',
              'district',
              'city',
              'tole',
              ) 
    list_display = ('province',
                     'district',
                     'city',
                     'tole',
                    ) 