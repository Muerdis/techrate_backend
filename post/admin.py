from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from post.models import Tag
from post.models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("text",)


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
