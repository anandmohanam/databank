from django.contrib import admin

from personal.models import Data



class table_data(admin.ModelAdmin):
    list_display = ('name', 'place', 'age','dob', 'job')

    def has_delete_permission(self, request, obj=None):
            return True

    def has_change_permission(self, request, obj=None):
        return True




admin.site.site_header = 'Admin'
admin.site.site_title = 'Django Admin'
admin.site.index_tittle = 'Welcome to the django Admin portal'

admin.site.register(Data,table_data)