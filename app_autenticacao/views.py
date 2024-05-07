from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

    
def loginuser(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("Falha no login. Por favor, verifique seu nome de usuário e senha.")
            else:
                return render(request, 'login.html', {'form': form})
            
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})
    
def home(request):
    return render(request, 'home.html')

def registro(request):
   
    if request.method == 'GET':
        return render(request, 'registro.html')

    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validação manual dos dados
        user= User.objects.filter(username=username).first()
        if user:
            return HttpResponse('usuario ja existe')
        
        # Cria o usuário com senha criptografada
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse('usuario cadastrado com sucesso')
    

    
def logalt(request):
    logout(request)
    return redirect('home')
