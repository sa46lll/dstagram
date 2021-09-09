from django.contrib import admin

from photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']  # ForeignKey 를 검색기능으로 선택
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created'] # 검색할 필드 선택(foreignKey 제외)
    ordering = ['updated', '-created']


admin.site.register(Photo, PhotoAdmin)
