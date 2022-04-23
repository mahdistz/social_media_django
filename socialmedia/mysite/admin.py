from django.contrib import admin
from .models import User, Post, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)

#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}  # write slug same of title automatically
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}  # write slug same of title automatically
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}  # write slug same of title automatically
