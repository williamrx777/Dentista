from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProntuarioForm
from .models import Prontuario
from django.contrib import messages
# Create your views here.

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/prontoarios/')
        if request.user.is_authenticated:
            return redirect('/prontoarios/')
        else:
            msg = 'Usuario ou senha incorreto.'
            return render(request, 'login.html', {'msg':msg})
    pass

def sair(request):
    logout(request)
    return redirect('/')
    pass


@login_required
def prontuario_list(request):
    nome = request.GET.get('nome')
    cpf = request.GET.get('cpf')
    prontuarios = Prontuario.objects.all()
    if nome:
        prontuarios = Prontuario.objects.filter(nome__icontains=nome)
    if cpf:
        prontuarios = Prontuario.objects.filter(cpf__icontains=cpf)
    return render(request, 'prontuario_list.html', {'prontuarios': prontuarios})

def prontuario_detail(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    return render(request, 'prontuario_detail.html', {'prontuario': prontuario})

@login_required
def prontuario_create(request):
    if request.method == "POST":
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Prontuário criado com sucesso!")
            return redirect('prontuario_list')
        else:
            # Adicione debug para visualizar os erros
            print(form.errors)  # Para visualizar no terminal
            messages.error(request, f"Erro ao criar prontuário: {form.errors}")
    else:
        form = ProntuarioForm()
    return render(request, 'prontuario_form.html', {'form': form})

@login_required
def prontuario_update(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    if request.method == "POST":
        form = ProntuarioForm(request.POST, instance=prontuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Prontuário atualizado com sucesso!")
            return redirect('prontuario_list')
    else:
        form = ProntuarioForm(instance=prontuario)
    return render(request, 'prontuario_form.html', {'form': form})
@login_required
def prontuario_delete(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    if request.method == "POST":
        prontuario.delete()
        messages.success(request, "Prontuário deletado com sucesso!")
        return redirect('prontuario_list')
    return render(request, 'prontuario_confirm_delete.html', {'prontuario': prontuario})
