from django.contrib import admin
from .models import Category, Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    # We tell django which field will be pre-populated and what fields will be populated from
    # i.e prepopulate the slug field using the title field. The title field is a tuple because the slug can be created from many fields
    prepopulated_fields = {'slug' : ('title',)}
    # To edit the display on the jango admin platfrom we can use the list_display 
    list_display = ("title", "category","author","status","is_featured")
    search_fields = ("id","title","status","category__category_name")
    # A tuple must have a comma at the end if there is only one item.
    list_editable = ("is_featured",)


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)