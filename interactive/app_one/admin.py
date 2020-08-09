from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
from .models import Video_item


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, PostAdmin)


# Video
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video_item, MyModelAdmin)