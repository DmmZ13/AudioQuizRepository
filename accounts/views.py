from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from datetime import datetime
import os, shutil
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UsuarioForm
from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Usuario

from django.shortcuts import render, redirect
from .forms import UsuarioForm

def registro_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecione para a página de login
    else:
        form = UsuarioForm()
    return render(request, 'accounts/signup.html', {'form': form})

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'