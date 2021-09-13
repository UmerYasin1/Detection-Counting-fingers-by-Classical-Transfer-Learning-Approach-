from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
import random
import os
from .model_file import *

def index(request):

    d= "Resuilts"

    a = random.randint(0, 5)

    if request.method == 'POST':

        form = input_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        path = os.listdir("D:/University Data/Comsats Lahore/Final Year Project/webapp/myapp/media/images")
        path1 = "D:/University Data/Comsats Lahore/Final Year Project/webapp/myapp/media/images/{}"

        # c = predict_image(path1.format(path[0]))

        c = pridict(path1.format(path[0]))

        if c == 0 or c == 1:
            c = 0
            if a == c:

                d = "WOW !! Input Matched Detected Zero Fingures"

        elif c == 2 or c == 3:

            c = 1

            if a == c:

                d = "WOW !! Input Matched Detected One Fingures"

        elif c == 4 or c == 5:

            c = 2

            if a == c:

                d = "WOW !! Input Matched Detected two Fingures"

        elif c == 6 or c == 7:

            c = 3

            if a == c:

                d = "WOW !! Input Matched Detected three Fingures"

        elif c == 8 or c == 9:

            c = 4

            if a == c:

                d = "WOW !! Input Matched Detected four Fingures"

        elif c == 10 or c == 11:
            c = 5

            if a == c:

                d = "WOW !! Input Matched Detected five Fingures"
        else:

            d = "Invalid Input"

        return d

    else:

        form = input_Form()

    return render(request, 'detection/index.html', {'form' : form , 'sign': d , 'random': a})




