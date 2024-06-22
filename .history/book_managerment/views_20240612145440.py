from django.shortcuts import render,HttpResponse,redirect
from .models import Book


def addbook(request):
    print(Book)
    if request.method.lower() == 'post':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')

        Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)
        return redirect('/selectbook/')
        # return HttpResponse('{}-{}-{}-{}'.format(title,price,pub_date,publish))

    return render(request,'addbook.html')


def selectbook(request):
    book_list = Book.objects.all()
    return render(request,'selectbook.html',locals())


def delbook(request,id):

    Book.objects.filter(id=id).delete()
    return redirect('/selectbook/')


def changebook(request,id):
    book_obj = Book.objects.filter(id=id).first()

    if request.method.lower() == 'post':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')

        Book.objects.filter(id=id).update(title=title,price=price,pub_date=pub_date,publish=publish)
        return redirect('/selectbook/')

    return render(request,'changebook.html',locals())


# Create your views here.


