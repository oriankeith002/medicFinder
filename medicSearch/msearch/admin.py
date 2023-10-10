from django.contrib import admin
from .models import *


# admin panel customization

class ProfileAdmin(admin.ModelAdmin):
#     # date_hierarchy = 'created_at' # create a hierarchy filter with dates
#     list_display = ('user','role','birthday',)
#     list_display_links = ('user','role',)
    pass



# Register your models here.

admin.site.register(Profile, ProfileAdmin);
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Speciality)
admin.site.register(Rating)