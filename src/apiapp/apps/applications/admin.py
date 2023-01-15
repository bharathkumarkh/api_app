from django.contrib import admin

from .models import App, Tasks

# Register your models here.
admin.site.register(App)
admin.site.register(Tasks)
