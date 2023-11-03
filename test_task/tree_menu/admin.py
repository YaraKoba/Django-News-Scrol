from django.contrib import admin
from tree_menu.models import MenuGroup, MenuItem


# Отображение компонентов в админке
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'group', 'parent', 'get_children')
    # авто заполнение поля slug
    prepopulated_fields = {'slug': ("text",)}


# Отображение групп в админке
class MenuGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # авто заполнение поля slug
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuGroup, MenuGroupAdmin)
