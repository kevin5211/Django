from django.contrib import admin
from .models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo #定义多的对象及个数
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
    inlines = [HeroInfoInline] #关联对象，一对多，指定多的对象

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)