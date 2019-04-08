from django.contrib import admin

# Register your models here.


from .models import Post, Tag, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# admin.register(Post)
# admin.register(Tag)
# admin.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)

