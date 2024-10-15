from django.shortcuts import render
import random
import string
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.

# Password generation logic
def generate_password(request):

    # Get the length parameter from the request and convert it to an integer
    length = int(request.GET.get('length', 8))  # Default length of 8 if not provided

    # Ensure the length is within a reasonable range
    if length < 4:
        length = 4
    elif length > 128:
        length = 128

    # Characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    escaped_password = escape(password)
    return HttpResponse(escaped_password)


def index(request):
    return render(request, 'generator/index.html')