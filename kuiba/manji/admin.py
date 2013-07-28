from django.contrib import admin
from models import FindaoUserInfo, FindaoTag, FindaoShare

class ShareAdmin(admin.ModelAdmin):
    list_display = ['whoes', 'title', 'ctime']

admin.site.register(FindaoUserInfo)
admin.site.register(FindaoTag)
admin.site.register(FindaoShare,ShareAdmin)
