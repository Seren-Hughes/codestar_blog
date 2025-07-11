from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    search_fields = [
        "title",
        "content",
        "slug",
        "author__username",
        "created_on",
        "updated_on",
        "status",
    ]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.
admin.site.register(Comment)
