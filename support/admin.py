from django.contrib import admin

from .models import Support, models


class SupportAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Support, SupportAdmin)


class ShowMorpheme(models.Model):
    permissions = (
        ("show_morpheme", "morph Show to Main Menu"),
    )


class ShowML(models.Model):
    permissions = (
        ("show_ml", "ml Show to Main Menu"),
    )


class ShowRTC(models.Model):
    permissions = (
        ("show_rtc", "rtc Show to Main Menu"),
    )
