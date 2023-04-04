from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article(models.Model):
    titre = models.CharField(max_length=255)
    titre_tag = models.CharField(max_length=255, default="blog")
    contenu = RichTextField(blank=True, null=True)
    # contenu = models.TextField()
    slug = models.SlugField(unique=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', max_length=60, on_delete=models.CASCADE, null=True)
    extrait = models.CharField('Category', max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_articles')

    def __str__(self):
        return self.titre + ' - ' + str(self.auteur)

    def get_absolute_url(self):
        # return reverse('article_details', args=(str(self.id)))
        return reverse('accueil')

    def total_likes(self):
        return self.likes.count()

class Category(models.Model):
    nom = models.CharField(max_length=60)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('accueil')

    class Meta:
        verbose_name_plural = 'Categories'

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    github_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True, max_length=255)
    pinterest_url = models.CharField(null=True, blank=True, max_length=255)
    twitter_url = models.CharField(null=True, blank=True, max_length=255)
    website_url = models.CharField(null=True, blank=True, max_length=255)
    youtube_url = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('accueil')

class Commentaire(models.Model):
    article = models.ForeignKey(Article, related_name="commentaires", on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    contenu = models.TextField()
    commentaire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.article.titre, self.nom)
