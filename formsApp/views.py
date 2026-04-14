from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Login
from .forms import Loginform
# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));

def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)

        #validate email
        if form.is_valid():
            form.save()
            print("Login info saved")
        else:
            print("invalid form")

        email = request.POST.get("email")
        password = request.POST.get("password")


        Login.objects.create(email=email, password=password)
        context = {"useremail": email}
        template = loader.get_template("details.html");
        return HttpResponse(template.render(context, request));

def details(request):
    detailsList = Login.objects.all()
    context = {"details": detailsList}
    template = loader.get_template("details.html");
    return HttpResponse(template.render(context, request));
