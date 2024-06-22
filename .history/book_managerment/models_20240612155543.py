from django.db import models


class Book(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('书名', max_length=64, null=True)
    ISBN = models.CharField('ISBN编号', max_length=64)
    author = models.CharField('作者', max_length=64)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)  # Django中创建外键联表操作
    publish_date = models.DateField('出版日期', max_length=64,blank=True)
    catagoery = models.CharField('类别', max_length=64)
    picture = models.ImageField('图片', upload_to='static/images', blank=True)
    
class LmsUser(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('姓名', max_length=32)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱')
    mobile = models.IntegerField('手机', max_length=11)
    borrow_num = models.IntegerField('借书数量', max_length=11)
    is_allow_borrow = models.BooleanField('是否允许借书', default=True)
    #is_admin = models.BooleanField('是否管理员', default=False)
    class_major = models.CharField('专业-班级', max_length=32)



class Author(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=4)
    age = models.IntegerField('年龄', default=0)
    tel = models.CharField('联系方式', max_length=64)
    # 一个作者可以对应多本书，一本书也可以有多个作者，多对多，在数据库中创建第三张表
    book = models.ManyToManyField(to=Book)
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/agelee/article/details/116453544


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
