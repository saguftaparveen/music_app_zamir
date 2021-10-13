from .forms import Loginform, Registerform
from django.shortcuts import redirect, render
# from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the post app.")

context={
   'question':"why this colaveri di"
}
def my_index(request):
    return render(request,'index.html',context)
contex={
    'name':"sagufta"
}
def about(request):
    return render(request,about.html,contex)


def signup(request):
    return render(request, 'signup.html')
def premium(request):
    return render(request,'premium.html')

# def manualform(request):
#     form=Loginform(request.POST or None)
#     context={"form":form}
#     if request.method=='POST':
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return HttpResponse("invalid")
#     else:
#         return render(request,'manual_form.html',context)

def manualform(request):

    form=Loginform(request.POST or None)
    if request.user.is_authenticated:
        return redirect("/artists/")


    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            try:
                user = authenticate(request, username=name, password=password)
                login(request, user)
                return redirect(reverse("my_index"))
            except:
                print("invalid credentials")

        else:
            print("invalid")

    context = {"form": form}
    return render(request, "manual_form.html", context)

def logoutview(request):
    if request.method=='POST':
        logout(request)
        return redirect(reverse('loginform'))

def registerview(request):

    form=Registerform(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('invalid')
            return redirect(reverse('registerform'))
    context={'form':form}
    return render(request,'registerform.html',context)