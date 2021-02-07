from django.shortcuts import render, redirect
from .models import Post, Arquivo
from .forms import PostForm, ArquivoForm


def listar_post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def detalhe_post(request, id):
    post = Post.objects.get(pk=id)
    arquivos = Arquivo.objects.filter(post_id=post.id)
    context = {
        'post': post,
        'arquivos': arquivos
    }
    return render(request, 'detalhe.html', context)


def novo_post(request):
    if request.method == 'POST':
        data = request.POST
        arquivos = request.FILES.getlist('arquivo')

        if data['titulo'] != 'none' and data['conteudo'] != 'none':
            post, created = Post.objects.get_or_create(
                conteudo=data['conteudo'],
                titulo=data['titulo'],
            )
            for arq in arquivos:
                arquivo = Arquivo.objects.create(
                    post=post,
                    arquivo=arq
                )
        return redirect('listar_post')
    return render(request, 'novo_post.html')


def novo_post2(request):
    form = PostForm(request.POST or None, request.FILES or None)
    form_file = ArquivoForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'form_file': form_file
    }
    if request.method == 'POST':
        data = request.POST
        arquivos = request.FILES.getlist('arquivo')
        if form.is_valid() and form_file.is_valid():
            post, created = Post.objects.get_or_create(
                titulo=data['titulo'],
                conteudo=data['conteudo'],
            )
            for arq in arquivos:
                arquivo = Arquivo.objects.create(
                    post=post,
                    arquivo=arq
                )
        return redirect('listar_post')
    return render(request, 'novo_post_form.html', context)
