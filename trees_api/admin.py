from django.contrib import admin

from .models import Tree


class TreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'species', 'genus', 'borough']


admin.site.register(Tree, TreeAdmin)
