from django.contrib import admin

from apps.vehicles.models import Automobilis, Vizitas

admin.site.register([Automobilis, Vizitas])
