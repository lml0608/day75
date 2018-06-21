from django.shortcuts import render,HttpResponse

# Create your views here.


def asset(request):

    print(request.method)
    print(request.POST)
    print(request.GET)


    return HttpResponse("OK")

