from django.contrib import admin

from post.models import Tag
from post.models import Post

admin.site.register(Tag)
admin.site.register(Post)
