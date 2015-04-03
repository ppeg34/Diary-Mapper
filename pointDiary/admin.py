from django.contrib.gis import admin
from models import Diary

# Register your models here.
admin.site.register(Diary, admin.OSMGeoAdmin)
