from django.db import models


# Create your models here.
class orderInfo(models.Model):
    customerName = models.CharField(max_length=100, verbose_name='收货人姓名')
    customerPhone = models.CharField(max_length=50, verbose_name='收货人电话')
    customerAddress = models.CharField(max_length=500, verbose_name='收货人地址')
    orderName = models.CharField(max_length=120, verbose_name='代理人姓名')

    def __unicode__(self):
        return self.customerName

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name
