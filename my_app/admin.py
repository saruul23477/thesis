from django.contrib import admin
from .models import users, research ,diplom , detail, plan

admin.site.register(users)
admin.site.register(research)
admin.site.register(diplom)
admin.site.register(detail)
admin.site.register(plan)