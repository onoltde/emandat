from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Competitions)
admin.site.register(Types)
admin.site.register(Comments)
admin.site.register(Profiles)
