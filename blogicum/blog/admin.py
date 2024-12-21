from django.contrib import admin
from .models import Post, Category, Location
from django.utils.translation import gettext_lazy as _

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category', 'location', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    search_fields = ('title',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category', 'location', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'text')
    fieldsets = (
        (None, {'fields': ('title', 'text', 'author', 'category', 'location', 'is_published')}),
        (_('Publication Info'), {'fields': ('pub_date', 'created_at')}),
    )
    verbose_name = _('публикация')
    verbose_name_plural = _('публикации')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    search_fields = ('title',)
    verbose_name = _('категория')
    verbose_name_plural = _('категории')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name',)
    verbose_name = _('местоположение')
    verbose_name_plural = _('местоположения')