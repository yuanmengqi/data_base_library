from django.shortcuts import render
from book_managerment import models
from django.shortcuts import redirect

## 出版社
# 出版社列表
def publisher_list(request): #处理用户提交的表单数据，将数据保存到数据库中的Book模型对象中，然后根据操作结果重定向用户到另一个页面或者返回一个包含表单的页面
    publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': publishers})

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
        return redirect('/pub_list/')
 
    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'pub_edit.html', {'publisher': edit_obj})

# 删除出版社
 
def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/pub_list/')