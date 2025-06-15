from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.GroupCategory)


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_name", "teacher", "category"]
    search_fields = ["group_name", "teacher", "category"]
    prepopulated_fields = {
        "slug": ("group_name", "days", "teacher", "time")
    }
