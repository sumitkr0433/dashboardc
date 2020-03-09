from django.contrib import admin
from .models import p_country,p_state,p_city,p_location
# Register your models here.


admin.site.register(p_location)
admin.site.register(p_city)
admin.site.register(p_state)
admin.site.register(p_country)
