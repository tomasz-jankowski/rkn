from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Society


# admin.site.register(Society)

class SocietyAdmin(admin.ModelAdmin):
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 100px; max-height: 100px;" />')
        else:
            return 'No Image'
    logo_preview.allow_tags = True

admin.site.register(Society, SocietyAdmin)