from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

# Update the page admin display
class PageAdmin(admin.ModelAdmin):
    # fields = ['category', 'title', 'url']
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)

admin.site.register(Category)