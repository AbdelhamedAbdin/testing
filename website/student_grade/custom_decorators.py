from django.http import HttpResponseRedirect


def decoratorDirect(func):
    def wrapper(request, *args):
        if request.path == '/' and request.GET == {}:
            if 'page_number' not in request.GET:
                return HttpResponseRedirect('/?page_number=1')
        return func(request, *args)
    return wrapper
