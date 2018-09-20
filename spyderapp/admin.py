from django.contrib import admin

from .models import Patron, Associates

admin.site.register([Patron, Associates])
 