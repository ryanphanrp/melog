from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['body', 'time']
    list_filter = ['time']
    search_fields = ['body']
    
admin.site.register(Post, PostAdmin)