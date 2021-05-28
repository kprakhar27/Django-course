from django.http import HttpResponse, response
from django.shortcuts import render


# Create your views here.
def index(request):
    developed_by = 'Kumar Prakhar'
    members = [
        'Kumar Prakhar', 'Rahul Mandviya', 'Abhinav Gadgil', 'Rohan Sarkar'
    ]
    show_developer = False

    context = {
        'developer': developed_by,
        'members': members,
        'show_developer': show_developer
    }
    response = render(request, 'HelloWorld/index.html', context)
    return response


def hello(request):
    return render(request, 'HelloWorld/hello.html')