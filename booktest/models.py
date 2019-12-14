from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) #字符串类型
    bpub_date = models.DateField()
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo) #定义成一个类型 通过外键指定
    def __str__(self):
        return self.hname