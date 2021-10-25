from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from api.forms import TodoForm
from api.models import Todo

PAGE_SIZE = 10


@login_required
@require_http_methods(["GET", "POST"])
def index(request):
    form = TodoForm()
    form.instance.user_id = request.user.id

    return render(request,
                  'api/index.html',
                  {
                      "forms": form,
                      "list": Todo.objects.filter(user_id=request.user.id).order_by("-date")[0:PAGE_SIZE],
                      "title": "TODO LIST"
                  })


@login_required
@require_http_methods(["POST"])
def add(request):
    form = TodoForm(request.POST)
    valid = form.is_valid()

    if valid:
        todo: Todo = form.save(commit=False)
        todo.user_id = request.user.id
        todo.save()

    return render(
        request=request,
        template_name='api/tasks.html',
        context={
            "forms": form,
            "list": Todo.objects
                        .filter(user_id=request.user.id)
                        .order_by("-date")[0:PAGE_SIZE],
            "title": "TODO LIST"
        },
        status=(HTTPStatus.CREATED if valid else HTTPStatus.BAD_REQUEST)
    )


# noinspection PyUnusedLocal
@login_required
@require_http_methods(["POST", "DELETE"])
def remove(request, item_id):
    item: Todo = Todo.objects.get(id=item_id)
    item.delete()

    return HttpResponse("", "text/plain", HTTPStatus.OK)


@login_required
@require_http_methods(["POST"])
def edit(request, item_id):
    todo: Todo = Todo.objects.get(id=item_id)

    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        todo: Todo = form.save(commit=False)
        todo.user_id = request.user.id
        todo.save()
        return render(request=request,
                      template_name='api/tasks.html',
                      context={
                          "forms": form,
                          "list": Todo.objects.order_by("-date")[0:PAGE_SIZE],
                      },
                      status=HTTPStatus.OK)

    return render(request=request,
                  template_name='api/form.html',
                  context={
                      "forms": form,
                      "item": todo
                  },
                  status=HTTPStatus.BAD_REQUEST)
