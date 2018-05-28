# from django.shortcuts import render, HttpResponse, redirect
# # the index function is called when root is visited
# def index(request):
#     response = "Hello, I am your second request!"
#     return HttpResponse(response)
# views.py
# from django.shortcuts import render, HttpResponse, redirect
# def index(request):
#     context = {
#         "email" : "blog@gmail.com",
#         "name" : "mike"
#     }
#     return render(request, "blogs/index.html", context)
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, time
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "tie" : get_random_string(length=14),
    }
    return render(request,'blogs/index.html', context)


def creat(request):
    def first(request):
        response = "Hello, I am your index request!"
        return HttpResponse(response)
