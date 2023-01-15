from applications.models import App
from django.shortcuts import render


def home(request):

    app_list = App.objects.all()
    context = {
        "object_list": app_list,
    }

    return render(request, "home.html", context=context)
