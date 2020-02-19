from django.shortcuts import render, redirect
from app_1.models import *


def index(request):
    return render(request, 'index.html')


def create(request):
    new_show = Show.objects.create(title = request.POST['title'], network=request.POST['network'], released_date=request.POST['released_date'], description=request.POST['description'])
    return redirect('/show/' + str(new_show.id))



def info(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'info.html', context)



def edit(request, id):
    context ={
        "show":Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)



def update(request, id):

    if request.POST:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.released_date = request.POST['released_date']
        show.description = request.POST['description']
        show.save()

        return redirect('/show/' + str(show.id))
    


def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()

    return redirect('/shows')



def shows(request):
    context = {
        'shows': Show.objects.all(),
    }

    return render(request, 'shows.html', context)

