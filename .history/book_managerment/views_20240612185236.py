from django.shortcuts import render
from book_managerment import models

def publisher_list(request):
    publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        new_publisher_addr = request.POST.get('addr')
        models.Publisher.objects.create(name=new_publisher_name, addr=new_publisher_addr)
        return redirect('/publisher_list/')
    return render(request, 'publisher_add.html')