from django.contrib import admin

# Register your models here.
from .models import Serial, Entry

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1
    max_num = 50

class SerialAdmin(admin.ModelAdmin):
    inlines = [
        EntryInline,
    ]

class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Serial, SerialAdmin)
admin.site.register(Entry, EntryAdmin)