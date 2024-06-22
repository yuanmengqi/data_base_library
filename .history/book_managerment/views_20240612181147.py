from django.shortcuts import render
from book_managerment import models
from django.conf.urls import url

def publisher_list(request):
    publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})