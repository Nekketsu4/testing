from django.contrib import admin

from .models import ListStore, RubricStore

class ListStoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(ListStore, ListStoreAdmin)
admin.site.register(RubricStore)
