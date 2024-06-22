from django.shortcuts import render
from book_managerment import models
from django.shortcuts import redirect

'''## 出版社
# 出版社列表
def publisher_list(request): #处理用户提交的表单数据，将数据保存到数据库中的Book模型对象中，然后根据操作结果重定向用户到另一个页面或者返回一个包含表单的页面
    publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher': publishers})

# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        new_publisher_addr = request.POST.get('addr')
        models.Publisher.objects.create(name=new_publisher_name, addr=new_publisher_addr)
        return redirect('/publisher_list/')
    return render(request, 'publisher_add.html')

# 编辑出版社
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('edit_name')
        new_addr = request.POST.get('edit_addr')
        edit_obj.name = new_name
        edit_obj.addr = new_addr
        edit_obj.save()
        return redirect('/publisher_list/')
 
    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'publisher_edit.html', {'publisher': edit_obj})

# 删除出版社
def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/publisher_list/')'''



## 图书增删改查
# 书籍的列表
def book_list(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book})
 
 
# 添加本书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_book_author = request.POST.get('author')
        new_book_publish_date = request.POST.get('publish_date')
        new_book_catagoery = request.POST.get('catagoery')
        publisher = request.POST.get('publisher')
        new_book_picture = request.FILES.get('picture')
        models.Book.objects.create(name=new_book_name, author=new_book_author, publish_date=new_book_publish_date, 
                                   catagoery=new_book_catagoery, publisher=publisher, picture=new_book_picture)
        return redirect('/book_list/')
    res = models.Publisher.objects.all()
    return render(request, 'book_add.html', {'publisher_list': res})
 
 
# 删除本书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')
 
 
# 编辑本书籍
def edit_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_book_author = request.POST.get('author')
        new_book_date = request.POST.get('publish_date')
        new_publisher = request.POST.get('publisher')
        new_book_catagoery = request.POST.get('catagoery')
        new_book_picture = request.FILES.get('picture')
        edit_id = request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.author = new_book_author
        edit_obj.publish_date = new_book_date
        edit_obj.publisher = new_publisher
        edit_obj.catagoery = new_book_catagoery
        edit_obj.picture = new_book_picture
        edit_obj.save()
        return redirect('/book_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    #all_publisher = models.Publisher.objects.all()
    return render(request, 'book_edit.html', {'book': edit_obj, 'publisher_list': all_publisher})