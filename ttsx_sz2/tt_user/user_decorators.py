from django.shortcuts import redirect,render

def is_login(fn):
    def fun2(request,*args,**kwargs):
        if 'uid' in request.session:
            return fn(request,*args,**kwargs)
        else:
            # return render(request,'tt_user/qu_login.html')
            return redirect('/user/login/')
    return fun2

