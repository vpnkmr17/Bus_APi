from django.contrib import admin
from .models import BusNo,StopName,Route
# Register your models here.
admin.site.register(BusNo)

#admin.site.register(Route)

class StopNameAdmin(admin.ModelAdmin):
    list_display=('stop_name',)
    search_fields = ('stop_name', )
admin.site.register(StopName,StopNameAdmin)
class RouteNameAdmin(admin.ModelAdmin):
    list_display=('stop_id','bus_id',)
    search_fields = ('stop_id', )
admin.site.register(Route,RouteNameAdmin)