from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AccueilView, AddArticleView, ArticleDetailView, UpdateArticleView, DeleteArticleView, AddCategoryView, CategoryView, CategoryListView, LikeView, CreateCommentaireView

urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_article/', AddArticleView.as_view(), name='add_article'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    # path editer l'article
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name='edit_article'),
    path('article/<int:pk>/remove', DeleteArticleView.as_view(), name='delete_article'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_article'),
    path('article/<int:pk>/commentaire/', CreateCommentaireView.as_view(), name='create_commentaire'),
    ] + static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
