from django.contrib import admin

# Register your models here.
from .models import Services,News

admin.site.register(Services)
admin.site.register(News)