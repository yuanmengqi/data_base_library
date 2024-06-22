from django.shortcuts import render
from book_managerment import models

def publisher_list(request):
    publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})