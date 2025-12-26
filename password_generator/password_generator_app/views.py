import random
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def password(request):
    # Initialize the character pool with lowercase letters
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    # If 'uppercase' checkbox is checked, add uppercase letters to the character pool
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # If 'special' checkbox is checked, add special characters to the character pool
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    # If 'numbers' checkbox is checked, add digits to the character pool
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # Get the desired password length from GET parameters, default to 12 if not provided
    length = int(request.GET.get('length', 12))

    # Initialize an empty string to build the password
    the_password = ''
    
    # Loop through the desired length and randomly select characters from the pool
    for x in range(length):
        the_password += random.choice(characters)

    # Render the password template and pass the generated password as context
    return render(request, 'password.html', {'password': the_password})