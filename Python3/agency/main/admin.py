from django.contrib import admin

# Register your models here.
from .models import orderInfo

class orderInfoAdmin(admin.ModelAdmin):
    list_display = (
        'customerName', 'customerPhone', 'customerAddress','orderName'
    )
    search_fields = (
        'customerName', 'customerPhone', 'customerAddress','orderName'
    )
    list_filter = (
        'customerName', 'customerPhone', 'customerAddress', 'orderName'
    )

admin.site.register(orderInfo,orderInfoAdmin)
admin.site.site_header = '代理下单系统后台管理'
admin.site.site_title = '代理下单系统后台管理'