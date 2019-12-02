from django.contrib import admin
from blogging.models import Post, Category

## and a new admin registration
# admin.site.register(Post)
# admin.site.register(Category)


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
       CategoryInLine,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
       CategoryInLine, 
    ]    
    exclude = ('posts',) 
