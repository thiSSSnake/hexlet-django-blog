from django.urls import path
from hexlet_django_blog.article import views
# from hexlet_django_blog.article.views import ArticleView


urlpatterns = [
    # path('', ArticleView.as_view()),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
