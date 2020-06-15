from django.contrib import admin

# Register your models here.
from blog.models import Categorie, Article, ArticleAdmin

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
