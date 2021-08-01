from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")

    if request.method == "POST":

        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('todo')

    form = TodoForm()

    page = {

        "forms": form,

        "list": item_list,

        "title": "TODO LIST",

    }

    return render(request, 'api/index.html', page)


def add(request):
    item_list = Todo.objects.order_by("-date")

    if request.method == "POST":

        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

    #            return redirect('todo')

    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'api/tasks.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)

    item.delete()

    messages.info(request, "Item removed!!!")

    return HttpResponse("", "text/plain", 201)


def edit(request, item_id):
    item = Todo.objects.get(id=item_id)

    item_list = Todo.objects.order_by("-date")

    if request.method == "POST":

        form = TodoForm(request.POST, instance=item)

        if form.is_valid():
            item.save()
            return render(request, 'api/tasks.html', {
                "forms": form,
                "list": item_list,
            })

    form = TodoForm(instance=item)

    page = {
        "forms": form,
        "item": item
    }

    return render(request, 'api/form.html', page)
