from django.shortcuts import render
# from django.http import *
# from django.template import RequestContext,loader
from .models import *
# Create your views here.

def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList = BookInfo.objects.all()
    content = {
        'list':bookList
    }
    return render(request,'booktest/index.html',content)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    content = {
        'list':herolist
    }
    return render(request,'booktest/show.html',content)
