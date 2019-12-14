from django.contrib import admin
from .models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo #�����Ķ��󼰸���
    extra = 10
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline] #��������һ�Զָ࣬����Ķ���

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)