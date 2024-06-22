from django.db import models


class Book(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('书名', max_length=64, null=True)
    ISBN = models.CharField('ISBN编号', max_length=64)
    translator = models.CharField('译者', max_length=64)
    date = models.DateField('出版日期', max_length=64,blank=True)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)  # Django中创建外键联表操作


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,unique=True)
    # state = models.BooleanField()
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=2)  # 最大值为999999.99 总共8个数字，其中包含小数点有两个
    publish = models.CharField(max_length=32)
