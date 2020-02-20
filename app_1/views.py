from django.shortcuts import render, redirect, HttpResponse
from app_1.models import *
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def create(request):
    errors = (Show.objects.validator(request.POST))
    # .update(Show.objects.unique_title_validator(request.POST))
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/show/new')
    else:
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
        errors = Show.objects.validator(request.POST)
        # show = Show.objects.get(id=id)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/show/' + str(id) + '/edit')

        else:
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

