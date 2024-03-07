from django.contrib import admin
from .models import Post, Category, Comment, About, Privacy, Terms

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date_created')
    list_filter = ("status",)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_created', 'active')
    list_filter = ('active', 'date_created', 'date_updated')
    search_fields = ('name', 'body')



admin.site.register(About)
admin.site.register(Privacy)
admin.site.register(Terms)
