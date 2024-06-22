from django.db import models

'''class Publisher(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=64)
    addr = models.CharField('地址', max_length=64)'''
    
class Book(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('书名', max_length=64, null=True)
    author = models.CharField('作者', max_length=64)
    #publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)  # Django中创建外键联表操作
    publisher = models.CharField('出版社', max_length=64)
    publish_date = models.DateField('出版日期', max_length=64,blank=True)
    catagoery = models.CharField('类别', max_length=64)
    picture = models.ImageField('图片', upload_to='static/images', blank=True)
    
class LmsUser(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('姓名', max_length=32)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱')
    mobile = models.IntegerField('手机', default=0)
    borrow_num = models.IntegerField('借书数量', default=0)
    is_allow_borrow = models.BooleanField('是否允许借书', default=True)
    #is_admin = models.BooleanField('是否管理员', default=False)
    class_major = models.CharField('专业-班级', max_length=32)

class Borrow(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(to=LmsUser, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    borrow_date = models.DateField('借书日期', max_length=64)
    return_date = models.DateField('还书日期', max_length=64)
    is_return = models.BooleanField('是否归还', default=False)
    is_overtime = models.BooleanField('是否超时', default=False)
    is_renew = models.BooleanField('是否续借', default=False)
    renew_date = models.DateField('续借日期', max_length=64)

class appointment(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(to=LmsUser, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)

class overdue(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(to=LmsUser, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    borrow_date = models.DateField('借书日期', max_length=64)
    return_date = models.DateField('还书日期', max_length=64)
    is_return = models.BooleanField('是否归还', default=False)
    is_overtime = models.BooleanField('是否超时', default=False)
    is_renew = models.BooleanField('是否续借', default=False)
    renew_date = models.DateField('续借日期', max_length=64)
    fine = models.IntegerField('罚款金额', default=0)

class administor(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('姓名', max_length=32)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱')