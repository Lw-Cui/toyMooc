from django.contrib import admin
from models import Course, UserProfile

class CouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'image')

admin.site.register(Course, CouseAdmin)
admin.site.register(UserProfile)