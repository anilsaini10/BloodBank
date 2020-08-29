from django.contrib import admin
from .models import NeedBlood, DonateBlood,GotBlood

# Register your models here.

admin.site.register(NeedBlood)
admin.site.register(DonateBlood)
admin.site.register(GotBlood)