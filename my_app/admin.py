from django.contrib import admin
from .models import Test

class TestModelAdmin(admin.ModelAdmin):
    list_fields = ('file',)

admin.register(Test, TestModelAdmin)
