from django.contrib import admin

# these lines added:

from django.contrib import admin
from .models import Food, Entry


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 3


class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'serving']}),
        ('Entry', {'fields': ['value'], 'classes': ['collapse']}),
    ]
    inlines = [EntryInline]


admin.site.register(Food, FoodAdmin)
