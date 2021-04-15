from django.contrib import admin

# Register your models here.

from django.contrib import admin
from api.models import Vacancy
from api.models import Company
# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Company)