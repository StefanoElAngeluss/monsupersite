from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, CreateCommentaireForm, EditForm
from .models import Article, Category, Commentaire

class AccueilView(ListView):
    model = Article
    template_name = 'accueil.html'
    ordering = '-published_date'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AccueilView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        staff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = staff.total_likes()

        liked = False
        if staff.likes.filter(id=self.request.user.id).exists(): # type: ignore
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
    # fields = '__all__'

class UpdateArticleView(UpdateView):
    model = Article
    form_class = EditForm
    template_name = 'edit_article.html'
    # fields = ['titre', 'titre_tag', 'slug', 'contenu', 'image', 'auteur']
    # fields = '__all__'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('accueil')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_articles = Article.objects.filter(category__nom__contains=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_articles':category_articles})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list':cat_menu_list})

def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))

class CreateCommentaireView(CreateView):
    model = Commentaire
    form_class = CreateCommentaireForm
    template_name = 'add_commentaire.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('accueil')