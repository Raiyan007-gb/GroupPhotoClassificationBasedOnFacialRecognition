from django.contrib import admin
from django.contrib import admin
from .models import PicsRelation, Picture, Event

# Register your models here.
admin.site.register(Picture)
admin.site.register(Event)
admin.site.register(PicsRelation)