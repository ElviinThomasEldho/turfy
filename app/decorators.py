from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('loginUser')

    return wrapper_func

def player_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        groups = None
        if request.user.groups.exists(): 
            groups = set(group.name for group in request.user.groups.all())
            for group in groups:
                print('Player', group)
                if 'Player' == group:
                    return view_func(request, *args, **kwargs)
        return redirect('loginUser')
    return wrapper_func

def turf_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        groups = None
        if request.user.groups.exists(): 
            groups = set(group.name for group in request.user.groups.all())
            for group in groups:
                print('Turf', group)
                if 'Turf' == group:
                    return view_func(request, *args, **kwargs)
        return redirect('loginUser')
    return wrapper_func
