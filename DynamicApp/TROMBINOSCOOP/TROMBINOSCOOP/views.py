from django.shortcuts import render
from .forms import LoginForm


def welcome(request):
    return render(request, "welcome.html")

def login(request):
    """# teste pour savoir su=i le formulaire est envoyé
    if len(request.POST)>0:
        # teste si les paramettres attendus ont été envoyé
        if "email" not in request.POST or "password" not in request.POST:
            error = "Veuillez entrer une addresse de courriel et un mot de passe."
            return render(request, 'login.html', {"error": error})
        else:
            email = request.POST["email"]
            password = request.POST["password"]
            # teste si le mot de passe est le bon
            if password != 'alkaba' or email != 'mail@domain.com':
                error = "Adresse de couriel ou mot de passe invalide."
                return render(request, 'login.html', {"error": error})
            # si tout est bon
            else:
                return redirect('/welcome')
    # le formulaire n'a pas été envoyé
    else:
        return render(request, 'login.html')"""
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
