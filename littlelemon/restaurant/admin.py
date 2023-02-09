from django.contrib import admin

# Register your models here.
from .models import BookingTable, MenuTable

#Add the models so that they may be viewed in the admin site
admin.site.register(BookingTable)
admin.site.register(MenuTable)



