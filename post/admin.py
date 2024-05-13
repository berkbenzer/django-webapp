from django.contrib import admin
from .models import yazi

class adminYazi(admin.ModelAdmin):

    class Meta:
        model = yazi

admin.site.register(yazi)
# Register your models here.
