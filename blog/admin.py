from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','description')

class PostComment(admin.ModelAdmin):
    readonly_fields = ('created_date',)
    list_display = ('text','author')

    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,PostComment)