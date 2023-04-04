from django import forms
from .models import Article, Commentaire
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'titre_tag', 'auteur', 'slug', 'category', 'contenu', 'extrait', 'image')
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un titre'}),
            'titre_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un tag'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'id':'current_user', 'value': '', 'type': 'hidden'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un slug sous forme de "titre-du-slug"'}),
            # 'auteur': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre contenu'}),
            'extrait': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'titre_tag', 'category', 'slug', 'auteur', 'contenu', 'extrait', 'image')

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un titre'}),
            'titre_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un tag'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer un slug sous forme de "titre-du-slug"'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'id':'current_user', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre contenu'}),
            'extrait': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre contenu'}),
        }

class CreateCommentaireForm(forms.ModelForm):
    class Meta:
        users = User.objects.all()
        model = Commentaire
        fields = ('nom', 'contenu')

        widgets = {
            # ajouter un select des utilisateurs pour le commentaire
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre nom'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Veuillez entrer votre commentaire'}),
        }
