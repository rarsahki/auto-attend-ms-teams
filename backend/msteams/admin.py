from django.contrib import admin
from msteams.models import Msteams
# Register your models here.
class Msteamsadmin(admin.ModelAdmin):
    list_display = ('subject','email','password','prof','time','days')

#Registering model
admin.site.register(Msteams,Msteamsadmin)