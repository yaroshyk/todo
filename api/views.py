from django.http import (
    Http404, HttpResponse, JsonResponse
)

# Create your views here.
def add(request):
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """
    return JsonResponse({'success': True})
