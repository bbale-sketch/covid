from django.contrib import admin

# Register your models here.
from catalog.models import Speaker, Speech



@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']



@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker')



    
