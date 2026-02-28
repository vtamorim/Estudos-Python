from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Verificar se é uma requisição de delete
        delete_id = request.POST.get('delete')
        if delete_id:
            try:
                usuario_delete = Usuario.objects.get(id_usuario=delete_id)
                usuario_delete.delete()
            except Usuario.DoesNotExist:
                pass
        else:
            # Cadastrar novo usuário
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            if nome and idade:
                try:
                    idade_int = int(idade)
                except (TypeError, ValueError):
                    idade_int = None
                if idade_int is not None:
                    Usuario.objects.create(nome=nome, idade=idade_int)

    usuarios_lista = {'usuarios': Usuario.objects.all().order_by('-id_usuario')}
    return render(request, 'usuarios/usuarios.html', usuarios_lista)