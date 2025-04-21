from django.contrib import admin

from apps.shorter.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "token", "link_count", "reversed_url")
    list_display_links = list_display[:2]

    readonly_fields = ("token", "reversed_url")
    search_fields = ("url", "token")

    @admin.display(description="Полная ссылка")
    def reversed_url(self, obj):
        return obj.reversed_url
