from django import forms
# from django.forms import ClearableFileInput
from .models import Post, Arquivo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'titulo', 'conteudo'}
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }


class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = {'arquivo'}
        widgets = {
            'arquivo': forms.ClearableFileInput(attrs={
                'multiple': True,
                'class': 'form-control-file'
            })
        }