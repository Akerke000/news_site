from django.contrib import admin
from .models import Post, PostAttachment

# Register your models here.
admin.site.register(PostAttachment)
@admin.register(Post)

class CustomPostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {'fields' : ('title', 'content')}),
        ('Дополнительная информация', {'fields' : ('time_stamp', 'edited')}),
    )
    add_fieldsets = (
        ('Основная информация', {'fields' : ('title', 'content')}),
    )

    list_display = ('title', 'time_stamp', 'edited')

    search_fields = ('title', 'content')

    ordering = ('-time_stamp',)

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets