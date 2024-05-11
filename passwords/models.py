from django.db import models


class PasswordEntry(models.Model):
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class TheUserEntry(models.Model):
    theusername = models.CharField(max_length=50)
    thepassword = models.CharField(max_length=50)


class ZhangDna(models.Model):
    Shouzhi = models.CharField(max_length=100)
    Leixing = models.CharField(max_length=100)
    Jiage = models.CharField(max_length=100)


class Notebook(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="名")
    last_name = models.CharField(max_length=100, verbose_name="姓")
    email = models.EmailField(verbose_name="电子邮件")
    phone_number = models.CharField(max_length=20, verbose_name="电话号码")
    company = models.CharField(max_length=100, blank=True, verbose_name="公司")
    notes = models.TextField(blank=True, verbose_name="备注")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


from django.db import models

class Addresss(models.Model):
    name = models.CharField(max_length=100, verbose_name="收货人姓名")
    phone = models.CharField(max_length=15, verbose_name="手机号码")
    area = models.CharField(max_length=255, verbose_name="所在地区")
    address = models.TextField(verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="是否默认地址")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}的地址"