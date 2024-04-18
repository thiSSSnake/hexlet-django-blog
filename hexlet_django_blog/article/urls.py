from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView


urlpatterns = [
    # path('', ArticleView.as_view()),
    path('', IndexView.as_view()),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='article_update'),
    path('<int:article_id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
