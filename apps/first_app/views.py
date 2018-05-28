from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, time
from django.utils.crypto import get_random_string
import random

# the index function is called when root is visited


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
        words = {
            'random_word' : get_random_string(length=14).upper()

        }

    else:
        request.session['counter'] = 1
        words = {
            'random_word' : 'Lets Generate it'
        }


    return render(request, 'first_app/counter.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
