from django.shortcuts import redirect
from django.http import HttpResponse

def authenticated_user(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_fun(request)
        else:
            return redirect('/')
    return wrapper;
    
def admin_only(view_fun):
    def wrapper(request):
        if  request.user.groups.first().name == 'admin':
            return view_fun(request)

        if  request.user.groups.first().name == 'customer':
            return redirect('/customer_profile')
             
    return wrapper;

def allowed_roles(roles=[]):
    def decorator(view_fun):
        def wrapper(request,*args,**kwargs):
            if  request.user.groups.first().name in roles :
                return view_fun(request,*args,**kwargs) #orderCreate
            else :
                return HttpResponse('You are not authorized.')
        return wrapper;
    return decorator;