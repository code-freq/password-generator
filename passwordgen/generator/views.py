from string import digits

from django.shortcuts import render
import random
import string
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.html import escape

# Create your views here.

# Password generation logic
def generate_password(request):

    # Get the length parameter from the request and convert it to an integer
    length = int(request.GET.get('length', 8))  # Default length of 8 if not provided
    upper = request.GET.get("uppercase")
    lower = request.GET.get("lowercase")
    punc = request.GET.get("punctuation")
    digit = request.GET.get("digits")
    space = request.GET.get("space")

    # Length range
    if length < 4:
        length = 4
    elif length > 128:
        length = 128

    if upper or lower or digit or punc:
        # Characters to use in the password
        characters = ""
        if upper:
            characters += string.ascii_uppercase
        if lower:
            characters += string.ascii_lowercase
        if punc:
            characters += string.punctuation
        if digit:
            characters += string.digits
        if space:
            characters += " "

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        escaped_password = escape(password)
        return HttpResponse(f"<text class='success-message'>{escaped_password}</text>")

    else:
        return HttpResponse("<text class='error-message'>You must select at least one option except space!</text>")

def index(request):
    return render(request, 'generator/index.html')