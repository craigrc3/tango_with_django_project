from django.contrib import admin

# Register your models here.

from rango.models import Category, Page, UserProfile

# Update the page admin display
class PageAdmin(admin.ModelAdmin):
    # fields = ['category', 'title', 'url']
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)