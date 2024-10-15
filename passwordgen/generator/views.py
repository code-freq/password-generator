from django.shortcuts import render
import random
import string
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.

# Password generation logic
def generate_password(request):
    """
    View function to generate a password using the length parameter
    provided in the request. The length should be an integer between 4 and 128.
    If the length is not provided, a default length of 8 is used.

    Returns an HTTP response with the generated password.
    If the length is invalid, returns a 400 error.
    """
    try:
        # Get the length parameter from the request and convert it to an integer
        length = int(request.GET.get('length', 8))  # Default length of 8 if not provided

        # Ensure the length is within a reasonable range (e.g., between 4 and 128)
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
    except ValueError:
        return HttpResponse("Invalid length", status=400)



def index(request):
    """
    View function to render the main page of the password generator.

    Returns an HTTP response with the rendered HTML template.
    """
    return render(request, 'generator/index.html')