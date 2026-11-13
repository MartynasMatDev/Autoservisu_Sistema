from django.contrib import admin

from apps.accounts.models import Klientas, Meistras, Vadybininkas

admin.site.register([Klientas, Vadybininkas, Meistras])
