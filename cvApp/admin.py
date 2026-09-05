from django.contrib import admin

from cvApp.models import cv


# Register your models here.
@admin.register(cv)
class CvAdmin(admin.ModelAdmin):
    list_display = ('actualizado',)

    def has_add_permission(self, request):
        return not cv.objects.exists()
