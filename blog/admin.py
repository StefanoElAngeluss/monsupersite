from django.contrib import admin
from .models import Article, Category, Profile, Commentaire

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Commentaire)
